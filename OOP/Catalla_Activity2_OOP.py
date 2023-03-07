class Employee:
    __Name = ""
    __Gender = ""
    __Bdate = ""
    __Position = ""
    __Rate = 0
    __DaysWork = 0
    __gross = 0
    __SSS = 0
    __Tax = 0

    #getter
    #Employee Details
    def getName(self) -> str:
        return f"Name: {self.__Name}"

    def getGender(self) -> str:
        return f"Gender: {self.__Gender}"

    def getBdate(self) -> str:
        return f"Birth Date: {self.__Bdate}"

    def getPosition(self) -> str:
        return f"Position: {self.__Position}"

    def getGross(self) -> str:
        self.__gross = self.__DaysWork * self.__Rate
        return self.__gross
    
    #Employee Salary
    def getSSS(self) -> int:
        if self.__gross < 10_000:
            self.__S_SS = 500
            return f"SSS: {self.__SSS}"
        elif self.__gross < 20_000 >= 10_000:
            self.__SSS = 1000
            return f"SSS: {self.__SSS}"
        else:
            self.__SSS = 1500
            return f"SSS: {self.__SSS}"

    def getTax(self) -> int:
        if self.__gross < 10_000:
            self.__Tax = 0
            return f"Tax: {self.__Tax}"
        elif self.__gross < 20_000 >= 10_000:
            self.__Tax = self.__gross * 0.10
            return f"Tax: {self.__Tax}"
        elif self.__gross <= 30_000 >= 20_000:
            self.__Tax = self.__gross * 0.20
            return f"Tax: {self.__Tax}"
        else:
            self.__Tax = self.__gross * 0.30
            return f"Tax: {self.__Tax}"

    def getNetSalary(self) -> int:
        return f"Net Salary: {self.__gross - self.__SSS - self.__Tax}"

    #Details setter
    def setName(self, Name):
        self.__Name = Name
    def setGender(self, Gender):
        self.__Gender = Gender
    def setBdate(self, Bdate):
        self.__Bdate = Bdate
    def setPosition(self, Position):
        self.__Position = Position
    def setRate(self, Rate):
        self.__Rate = Rate
    def setDaysWork(self, DaysWork):
        self.__DaysWork = DaysWork


def main():
    #input
    e1 = Employee()
    e1.setName(input("Enter Employee Name: "))
    e1.setGender(input("Enter Employee Gender: "))
    e1.setBdate(input("Enter Employee Birth Date: "))
    e1.setPosition(input("Enter Employee Position: "))
    e1.setRate(int(input("Enter Employee Rate: ")))
    e1.setDaysWork(int(input("Enter Employee Days Work: ")))
    
    #displayEmployee Details
    print("\nEmployee Details\n")
    print(e1.getName(),e1.getGender(),e1.getBdate(),e1.getPosition(), sep='\n')
    
    #displaySalaryDetails
    print("\nEmployee Salary Details\n")
    print(e1.getGross(),e1.getSSS(),e1.getTax(),e1.getNetSalary(), sep='\n')
   
main()

