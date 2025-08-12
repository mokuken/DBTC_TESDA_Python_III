class Printer:
    def printDoc(self, document):
        pass

class Scanner:
    def scan(self, document):
        pass

class FaxMachine:
    def fax(self, document):
        pass

class AllInOneMachine(Printer, Scanner, FaxMachine):
    def printDoc(self, document):
        print("printing", document)

    def scan(self, document):
        print("scanning", document)

    def fax(self, document):
        print("facsmile", document)

class OldPrinter(Printer):
    def printDoc(self, document):
        print("printing", document)

print_all = AllInOneMachine()
scan_all = AllInOneMachine()
fax_all = AllInOneMachine()
print_all.printDoc("my docs")
scan_all.printDoc("my image")
fax_all.printDoc("fax docs")

print_doc = OldPrinter()
print_doc.printDoc("one document")