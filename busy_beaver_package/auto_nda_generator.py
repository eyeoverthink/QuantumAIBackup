"""
Auto-NDA Generator Module
===========================
Generates a basic Non-Disclosure Agreement (NDA) dynamically.
Copyright © 2025 Vaughn Scott | All Rights Reserved
"""

from datetime import datetime

class AutoNDAGenerator:
    def __init__(self, creator_name: str, project_name: str):
        self.creator_name = creator_name
        self.project_name = project_name
        self.date_today = datetime.utcnow().strftime("%B %d, %Y")

    def generate_nda_text(self, receiving_party: str) -> str:
        nda_template = f"""
        NON-DISCLOSURE AGREEMENT (NDA)

        This Non-Disclosure Agreement ("Agreement") is made effective as of {self.date_today} by and between {self.creator_name} ("Disclosing Party") and {receiving_party} ("Receiving Party").

        1. Definition of Confidential Information
        Confidential Information refers to any data, documentation, inventions, discoveries, trade secrets, patents, and intellectual property including but not limited to the "{self.project_name}" project.

        2. Obligations of Receiving Party
        The Receiving Party shall hold and maintain Confidential Information in strictest confidence for the sole and exclusive benefit of the Disclosing Party.

        3. No Transfer of Rights
        This Agreement does not transfer any rights, ownership, or licenses to the Receiving Party.

        4. Term
        The obligations of this Agreement shall survive for a period of five (5) years from the effective date.

        5. General Provisions
        This Agreement shall be governed by and construed in accordance with the laws of the jurisdiction of the Disclosing Party.

        IN WITNESS WHEREOF, the parties hereto have executed this Agreement as of the date first above written.

        Disclosing Party: {self.creator_name}
        Receiving Party: {receiving_party}

        """
        return nda_template


# Example usage
if __name__ == "__main__":
    generator = AutoNDAGenerator("Vaughn Scott", "Standalone Busy Beaver Calculator")
    nda_text = generator.generate_nda_text("Example Receiving Party")
    print(nda_text)