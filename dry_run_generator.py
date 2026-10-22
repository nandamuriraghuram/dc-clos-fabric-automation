"""
Offline Dry-Run Configuration Generator (Jinja2 + YAML Inventory)
Renders Arista EOS Underlay (eBGP) and Overlay (EVPN/VXLAN) configurations
for all Spine and Leaf switches without requiring live SSH connectivity.
"""
import yaml
from jinja2 import Environment, FileSystemLoader

TEMPLATES_TO_RENDER = ["interfaces.j2", "underlay.j2", "overlay.j2"]


def render_fabric_configs():
    with open("inventory/hosts.yml") as f:
        hosts = yaml.safe_load(f)
    with open("inventory/groups.yml") as f:
        groups = yaml.safe_load(f)

    env = Environment(
        loader=FileSystemLoader("templates"),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    for sw_name, host_obj in hosts.items():
        merged_data = {}
        for group_name in host_obj.get("groups", []):
            if group_name in groups and groups[group_name].get("data"):
                merged_data.update(groups[group_name]["data"])
        if host_obj.get("data"):
            merged_data.update(host_obj["data"])

        print("=" * 60)
        print(f" GENERATED ARISTA EOS CONFIG: {sw_name.upper()} ({host_obj.get('hostname')})")
        print("=" * 60)

        for tmpl_name in TEMPLATES_TO_RENDER:
            tmpl = env.get_template(tmpl_name)
            rendered = tmpl.render(host=merged_data, **merged_data)
            print(f"\n--- [Template: {tmpl_name}] ---")
            print(rendered.strip())
        print("\n")


if __name__ == "__main__":
    render_fabric_configs()
