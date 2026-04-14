# SDN-Based Firewall using POX Controller
---
## Problem Statement
Develop a controller-based firewall to block or allow traffic between hosts.

--- 
## 🎯 Objective

This project aims to:

* Implement an SDN firewall using a centralized controller (POX)
* Apply rule-based traffic filtering (IP-based)
* Dynamically install OpenFlow rules
* Handle `packet_in` events
* Demonstrate allowed and blocked traffic scenarios
* Maintain logs of blocked packets

---

## 🌐 Repository Link

https://github.com/Mitxh13/SDN-Based-Firewall-using-POX-Controller

---

## 📥 Clone Repository

```bash
https://github.com/Mitxh13/SDN-Based-Firewall-using-POX-Controller.git
cd SDN-Based-Firewall-using-POX-Controller
```

---

## ⚙️ System Requirements

* Ubuntu 22.04 / 24.04 (VM recommended)
* Mininet
* POX Controller
* Python 3.x

---

## 🛠️ Setup & Execution

### Step 1: Install Mininet

```bash
sudo apt update
sudo apt install mininet -y
```

---

### Step 2: Clone POX Controller

```bash
git clone https://github.com/noxrepo/pox
cd pox
```

---

### Step 3: Add Firewall Module

Copy `firewall.py` into:

```bash
pox/pox/misc/
```

---

### Step 4: Run Controller

```bash
cd pox
./pox.py misc.firewall log.level --DEBUG
```

---

### Step 5: Start Mininet Topology

(Open a new terminal)

```bash
sudo mn --topo single,3 --controller=remote,ip=127.0.0.1,port=6633
```

---

## 📁 Repository Structure

```
SDN-Based-Firewall-using-POX-Controller/
├── firewall.py
├── README.md
└── screenshots/
    ├── allowed_ping.png
    ├── blocked_ping.png
    ├── logs.png
    └── flows.png
```


---

## 🌐 Network Topology

* 3 Hosts: h1, h2, h3
* 1 Switch: s1
* Remote POX Controller

```
h1 ----\
        s1 ---- h3
h2 ----/
```

---

## 🔐 Firewall Rules

| Source IP | Destination IP | Action |
| --------- | -------------- | ------ |
| 10.0.0.1  | 10.0.0.2       | ALLOW  |
| 10.0.0.2  | 10.0.0.3       | BLOCK  |

---

## 🧪 Testing & Validation

### ✅ Scenario 1: Allowed Traffic

```bash
mininet> h1 ping h2
```

✔ Expected Result:

* Successful communication
* 0% packet loss

---

### ❌ Scenario 2: Blocked Traffic

```bash
mininet> h2 ping h3
```

✔ Expected Result:

* Communication blocked
* 100% packet loss

---

### 📊 Scenario 3: Throughput Test (iperf)

```bash
mininet> h1 iperf h2
mininet> h2 iperf h3
```

✔ Expected Result:

* h1 ↔ h2: Works
* h2 ↔ h3: Fails

---

## 📜 Controller Logs (Proof)

Example output:

```
Packet: 10.0.0.2 -> 10.0.0.3
BLOCKED: 10.0.0.2 -> 10.0.0.3
```

✔ Confirms firewall rule enforcement

---

## 🔄 Flow Table Verification

Run:

```bash
sudo ovs-ofctl dump-flows s1
```

✔ Shows installed OpenFlow rules:

* Forwarding rules (ALLOW)
* Drop rules (BLOCK)

---


## ✅ Conclusion

This project successfully demonstrates an SDN-based firewall where traffic control is centralized in the controller. It highlights how OpenFlow rules can be dynamically installed to enforce network security policies.

---

## 👨‍💻 Author

Mitesh

---

## ⚠️ Notes

* Tested on Ubuntu VM with Mininet and POX
* Ignore Python version warning in POX (does not affect functionality)
