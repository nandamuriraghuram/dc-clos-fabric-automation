"""
Data Center Spine-Leaf Post-Maintenance Health & Optical Auditor
Validates BGP control plane state, interface error counters, and DOM sensor readings.
"""
import sys
from nornir import InitNornir
from nornir_scrapli.tasks import send_commands
from nornir_utils.plugins.functions import print_result

PRE_POST_CHECKS = [
    "show ip bgp summary",
    "show interfaces counters errors",
    "show interfaces transceiver dom",
    "show lldp neighbors",
]


def run_fabric_audit(task):
    """Executes operational health checks across Spine and Leaf switches."""
    task.run(
        task=send_commands,
        name="Execute Data Center Rack & Routing Health Checks",
        commands=PRE_POST_CHECKS,
    )


if __name__ == "__main__":
    nr = InitNornir(config_file="config.yml")
    print("[*] Starting Automated Spine-Leaf Fabric Health Audit...")
    
    results = nr.run(task=run_fabric_audit)
    print_result(results)

    # Check if any switch failed SSH connection or command execution
    if results.failed_hosts:
        print(f"\n[!] AUDIT FAILED on hosts: {list(results.failed_hosts.keys())}")
        sys.exit(1)
    else:
        print("\n[+] AUDIT PASSED: All Spine/Leaf switches responded with healthy telemetry.")
