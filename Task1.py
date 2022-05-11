class Scanner:
    def scan(self):
        print('scan() method from Scanner class')


class Printer:
    def print(self):
        print('print() method from Printer class')


class Fax:
    def send(self):
        print('send() method from Fax class')

    def print(self):
        print('print() method from Fax class')


class MFD_SPF(Scanner, Printer, Fax):
    pass


class MFD_SFP(Scanner, Fax, Printer):
    pass


mfd_spf = MFD_SPF()
mfd_sfp = MFD_SFP()

mfd_spf.scan()    # 'scan() method from Scanner class'
mfd_spf.print()   # 'print() method from Printer class'
mfd_spf.send()    # 'send() method from Fax class'

mfd_sfp.scan()   # 'scan() method from Scanner class'
mfd_sfp.print()  # 'print() method from Fax class'
mfd_sfp.send()   # 'send() method from Fax class'