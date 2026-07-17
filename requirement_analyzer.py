import json
import os
import re


class RequirementGapAnalyzer:

    def __init__(self):

        self.storage = "analysis_history.json"

        self.history = []

        self.priority_keywords = {

            "High": [

                "must",

                "mandatory",

                "critical",

                "required",

                "essential"

            ],

            "Medium": [

                "should",

                "recommended",

                "important"

            ],

            "Low": [

                "optional",

                "nice to have",

                "future"

            ]

        }

        self.load_history()

    def load_history(self):

        if os.path.exists(self.storage):

            try:

                with open(

                    self.storage,

                    "r",

                    encoding="utf-8"

                ) as file:

                    self.history = json.load(file)

            except:

                self.history = []

    def save_history(self):

        with open(

            self.storage,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.history,

                file,

                indent=4

            )

    def read_requirements(self, title):

        print(f"\nEnter {title}")

        print("Press ENTER twice to finish.\n")

        lines = []

        while True:

            line = input()

            if line == "":

                break

            lines.append(line.strip())

        return [

            item

            for item in lines

            if item

        ]

    def normalize(self, text):

        text = text.lower()

        text = re.sub(

            r"[^a-z0-9 ]",

            "",

            text

        )

        return text.strip()

    def detect_priority(self, requirement):

        requirement = requirement.lower()

        for level in self.priority_keywords:

            for keyword in self.priority_keywords[level]:

                if keyword in requirement:

                    return level

        return "Unspecified"

    def analyze(self):

        print("\n========== REQUIREMENT GAP ANALYSIS ==========\n")

        client = self.read_requirements(

            "Client Requirements"

        )

        implemented = self.read_requirements(

            "Implemented Features"

        )

        normalized_features = [

            self.normalize(item)

            for item in implemented

        ]

        missing = []

        available = []

        priorities = []

        for requirement in client:

            normalized = self.normalize(

                requirement

            )

            found = False

            for feature in normalized_features:

                if normalized in feature or feature in normalized:

                    found = True

                    break

            if found:

                available.append(

                    requirement

                )

            else:

                missing.append(

                    requirement

                )

            priorities.append({

                "requirement": requirement,

                "priority": self.detect_priority(

                    requirement

                )

            })

        completion = 0

        if len(client) > 0:

            completion = round(

                (len(available) / len(client)) * 100,

                2

            )

        report = {

            "client_requirements": len(client),

            "implemented_features": len(implemented),

            "implemented": available,

            "missing": missing,

            "completion": completion,

            "priorities": priorities

        }

        self.history.append(

            report

        )

        self.save_history()

        print("\n========== ANALYSIS REPORT ==========\n")

        print("Client Requirements :", len(client))

        print("Implemented Features :", len(implemented))

        print("Coverage :", completion, "%")

        print()

        print("Implemented")

        print()

        if available:

            for item in available:

                print("-", item)

        else:

            print("None")

        print()

        print("Missing")

        print()

        if missing:

            for item in missing:

                print("-", item)

        else:

            print("None")

    def detect_duplicates(self, requirements):

        duplicates = []

        seen = set()

        for requirement in requirements:

            normalized = self.normalize(

                requirement

            )

            if normalized in seen:

                duplicates.append(

                    requirement

                )

            else:

                seen.add(

                    normalized

                )

        print("\n========== DUPLICATE REQUIREMENTS ==========\n")

        if duplicates:

            for item in duplicates:

                print("-", item)

        else:

            print("No Duplicate Requirements Found.")

    def detect_ambiguous_requirements(self):

        if not self.history:

            print("\nNo Analysis Available.")

            return

        latest = self.history[-1]

        vague_words = [

            "fast",

            "quick",

            "easy",

            "efficient",

            "good",

            "better",

            "user friendly",

            "secure",

            "modern",

            "simple"

        ]

        ambiguous = []

        for requirement in latest["implemented"] + latest["missing"]:

            sentence = requirement.lower()

            for word in vague_words:

                if word in sentence:

                    ambiguous.append(

                        requirement

                    )

                    break

        print("\n========== AMBIGUOUS REQUIREMENTS ==========\n")

        if ambiguous:

            for item in ambiguous:

                print("-", item)

        else:

            print("No Ambiguous Requirements Detected.")

    def estimate_complexity(self):

        if not self.history:

            print("\nNo Analysis Available.")

            return

        latest = self.history[-1]

        total = len(

            latest["implemented"]

        ) + len(

            latest["missing"]

        )

        high = 0

        medium = 0

        low = 0

        for item in latest["priorities"]:

            if item["priority"] == "High":

                high += 1

            elif item["priority"] == "Medium":

                medium += 1

            else:

                low += 1

        score = (

            high * 5

            + medium * 3

            + low

        )

        print("\n========== COMPLEXITY ==========\n")

        print("Total Requirements :", total)

        print("Estimated Complexity Score :", score)

        if score < 15:

            print("Project Complexity : Low")

        elif score < 35:

            print("Project Complexity : Medium")

        else:

            print("Project Complexity : High")

    def risk_analysis(self):

        if not self.history:

            print("\nNo Analysis Available.")

            return

        latest = self.history[-1]

        missing = len(

            latest["missing"]

        )

        coverage = latest["completion"]

        print("\n========== RISK ANALYSIS ==========\n")

        print("Coverage :", coverage, "%")

        print("Missing Requirements :", missing)

        if coverage >= 90:

            risk = "Low"

        elif coverage >= 70:

            risk = "Medium"

        elif coverage >= 50:

            risk = "High"

        else:

            risk = "Critical"

        print("Project Risk :", risk)

    def export_report(self):

        if not self.history:

            print("\nNo Analysis Available.")

            return

        latest = self.history[-1]

        with open(

            "requirement_gap_report.txt",

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                "========== REQUIREMENT GAP REPORT ==========\n\n"

            )

            file.write(

                f"Coverage : {latest['completion']}%\n\n"

            )

            file.write(

                "Implemented Requirements\n"

            )

            for item in latest["implemented"]:

                file.write(

                    f"- {item}\n"

                )

            file.write("\n")

            file.write(

                "Missing Requirements\n"

            )

            for item in latest["missing"]:

                file.write(

                    f"- {item}\n"

                )

            file.write("\n")

            file.write(

                "Priority Summary\n"

            )

            for item in latest["priorities"]:

                file.write(

                    f"{item['priority']} : {item['requirement']}\n"

                )

        print("\nReport Exported Successfully.")

    def dashboard(self):

        if not self.history:

            print("\nNo Analysis Available.")

            return

        latest = self.history[-1]

        print("\n========== DASHBOARD ==========\n")

        print(

            "Coverage :", latest["completion"], "%"

        )

        print(

            "Implemented :", len(

                latest["implemented"]

            )

        )

        print(

            "Missing :", len(

                latest["missing"]

            )

        )

        high = 0

        medium = 0

        low = 0

        unspecified = 0

        for item in latest["priorities"]:

            if item["priority"] == "High":

                high += 1

            elif item["priority"] == "Medium":

                medium += 1

            elif item["priority"] == "Low":

                low += 1

            else:

                unspecified += 1

        print()

        print("Priority Distribution")

        print("---------------------")

        print("High :", high)

        print("Medium :", medium)

        print("Low :", low)

        print("Unspecified :", unspecified)

    def clear_history(self):

        choice = input(

            "\nDelete Analysis History? (yes/no): "

        ).lower()

        if choice == "yes":

            self.history.clear()

            self.save_history()

            print("\nHistory Deleted Successfully.")

        else:

            print("\nOperation Cancelled.")