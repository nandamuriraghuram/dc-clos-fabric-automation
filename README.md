# Automated Data Center Spine-Leaf Fabric (Nornir, Scrapli & Containerlab)

An Infrastructure-as-Code (IaC) and network automation framework written in Python to provision, validate, and audit a Layer-3 Leaf-Spine (Clos) data center topology running eBGP Underlay and EVPN/VXLAN Overlay.

## Key Features
* **Zero-Touch Config Generation:** Dynamically renders multi-switch configurations (Base, Interfaces, eBGP Underlay, EVPN Overlay) using **Jinja2** templates and structured YAML inventory (`hosts.yml`, `groups.yml`).
* **High-Concurrency Deployment:** Pushes configurations concurrently across Spine and Leaf switches via **Nornir** and **Scrapli** (async SSH).
* **Automated Pre/Post-Maintenance Auditing (`audit_fabric_health.py`):** Collects live BGP neighbor states, LLDP topology mappings, interface error counters, and optical transceiver DOM metrics.
* **CI/CD Pre-Deployment Validation:** Integrates **Batfish** to test routing intent and configuration compliance prior to deployment.

## Tech Stack
* **Languages & Frameworks:** Python 3, Nornir, Scrapli, Jinja2, Batfish
* **Network OS & Emulation:** Arista cEOS, Containerlab, Docker
* **Protocols:** eBGP, MP-BGP EVPN, VXLAN, LLDP
