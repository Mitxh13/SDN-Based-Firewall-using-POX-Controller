from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

# MAC learning table
mac_to_port = {}

# Blocked IP pairs
blocked = [
    ("10.0.0.2", "10.0.0.3")
]

def _handle_PacketIn(event):
    packet = event.parsed
    in_port = event.port

    # Learn MAC address
    mac_to_port[packet.src] = in_port

    ip = packet.find('ipv4')

    if ip:
        src = str(ip.srcip)
        dst = str(ip.dstip)

        log.info(f"Packet: {src} -> {dst}")

        # BLOCK RULE
        if (src, dst) in blocked:
            log.info(f"BLOCKED: {src} -> {dst}")

            msg = of.ofp_flow_mod()
            msg.match.nw_src = src
            msg.match.nw_dst = dst
            # No actions = DROP

            event.connection.send(msg)
            return

    #  LEARNING SWITCH LOGIC
    if packet.dst in mac_to_port:
        out_port = mac_to_port[packet.dst]
    else:
        out_port = of.OFPP_FLOOD

    # Install flow
    msg = of.ofp_flow_mod()
    msg.match = of.ofp_match.from_packet(packet, in_port)
    msg.actions.append(of.ofp_action_output(port=out_port))

    event.connection.send(msg)

    # Send packet out
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=out_port))
    msg.in_port = in_port

    event.connection.send(msg)


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Firewall with Learning Switch Loaded")
