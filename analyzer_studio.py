from requirement_analyzer import RequirementGapAnalyzer


class AnalyzerStudio:

    def __init__(self):

        self.analyzer = RequirementGapAnalyzer()

    def display_menu(self):

        while True:

            print("\n")

            print("=" * 70)

            print("              REQUIREMENT GAP ANALYZER")

            print("=" * 70)

            print("1. Analyze Requirements")

            print("2. Detect Duplicate Requirements")

            print("3. Detect Ambiguous Requirements")

            print("4. Estimate Project Complexity")

            print("5. Risk Analysis")

            print("6. Dashboard")

            print("7. Export Report")

            print("8. Clear History")

            print("9. Exit")

            choice = input("\nEnter Choice : ").strip()

            if choice == "1":

                self.analyzer.analyze()

            elif choice == "2":

                client = self.analyzer.read_requirements(

                    "Requirements To Check"

                )

                self.analyzer.detect_duplicates(

                    client

                )

            elif choice == "3":

                self.analyzer.detect_ambiguous_requirements()

            elif choice == "4":

                self.analyzer.estimate_complexity()

            elif choice == "5":

                self.analyzer.risk_analysis()

            elif choice == "6":

                self.analyzer.dashboard()

            elif choice == "7":

                self.analyzer.export_report()

            elif choice == "8":

                self.analyzer.clear_history()

            elif choice == "9":

                print("\nThank You For Using Requirement Gap Analyzer!")

                break

            else:

                print("\nInvalid Choice. Please Try Again.")


if __name__ == "__main__":

    studio = AnalyzerStudio()

    studio.display_menu()