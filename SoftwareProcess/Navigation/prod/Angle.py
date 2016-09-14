#Joshua Ando 
#Testing in test
class Angle():
    
    string = ""
    degree = ""
    
    def __init__(self):
        #self.angle = ...       set to 0 degrees 0 minutes
        
        self.string = "0d0.0"
        self.setDegreesAndMinutes("0d0.0")
        
        pass
    
    def setDegrees(self, degrees):
        
        if degrees == "": 
            raise ValueError("Angle.setDegrees:  null string")
        
        var1 = degrees % 360
        var2 = str(degrees)
        a, b = var2.split(".",1)
        var3 = float(b)
        var3 = var3 * 60 
        var4 = float(a)
        var5 = round(var3, 1)
        var6 = str(a) + "d" + str(b)
        
        
        
        self.degree = var1 
        self.string = var6
        return var1
    
        pass
    
    def setDegreesAndMinutes(self, degrees):
        
        self.deg_testing(degrees) #checks test cases. 
        
        a, b = degrees.split("d",1)
        a_Num = float(a) if '.' in a else int(a)
        b_Num = float(b) if '.' in b else int(b)
        
        deg = a_Num % 360 
        min = (b_Num % 60.0) / 60.0
        min1 = round(min, 1)
        DM = deg + min1
        
        self.string = a + "d" + b
        self.degree = DM 
        pass
    
    def add(self, angle):
        if isinstance(angle, Angle)is False: 
            raise ValueError("Angle.subtract: not instance of Angle")
        
        var1 = self.string
        var2 = angle.string
        a, b = var1.split("d",1)
        c, d = var2.split("d",1)
        sum_Deg = (int(a) + int (c)) % 360 
        sum_MinString = ((float(b) + float(d)) % 60.0)
        sum_Min = ((float(b) + float(d)) % 60.0) / 60.0
        sum_M = round(sum_Min, 1)
        if float(b) + float(d) == 60.0: 
            sum_DM = sum_Deg + 1.0
        else: 
            sum_DM = sum_Deg + sum_M
        
        self.string = str(sum_Deg) + "d" + str(sum_MinString)
        self.degree = str(sum_DM)
        pass
    
    def subtract(self, angle):
        
        if isinstance(angle, Angle)is False: 
            raise ValueError("Angle.subtract: not instance of Angle")
        
        var1 = self.string
        var2 = angle.string
        a, b = var1.split("d",1)
        c, d = var2.split("d",1)
        sub_Deg = (int(a) - int(c)) % 360 
        sub_MinString = ((float(b) - float(d)) % 60.0)
        sub_Min = ((float(b) - float(d)) % 60.0) / 60.0
        sub_M = round(sub_Min, 1)
        if float(b) - float(d) == -30.0:
            sub_DM = (sub_Deg - 1) + sub_M
        else: 
            sub_DM = sub_Deg + sub_M
        
        self.string = str(sub_Deg) + "d" + str(sub_MinString) 
        self.degree = sub_DM
        pass
    
    def compare(self, angle):
        if isinstance(angle, Angle)is False: 
            raise ValueError("Angle.compare:  not instance of Angle")
        
        var1 = self.degree - angle.degree
        
        if var1 < 0: 
            return -1
        if var1 > 0: 
            return 1
        if var1 == 0: 
            return 0

        
        pass
    
    def getString(self):
        
        print self.string
        
        pass
    
    def getDegrees(self):
        
        print self.degree
        
        pass
    
    def deg_testing(self, degrees):
        if "d" not in degrees: 
            raise ValueError("Angle.setDegreesAndMinutes: no separator")
        a, b = degrees.split("d",1)
        
        if a == "": 
            raise ValueError("Angle.setDegreesAndMinutes:  null string")
        if b == "":
            raise ValueError("Angle.setDegreesAndMinutes: no minutes")
        if "d" not in degrees: 
            raise ValueError("Angle.setDegreesAndMinutes: no separator")
        
        a_Num = float(a) if '.' in a else int(a)
        if isinstance(a_Num,int) is False: 
            raise ValueError("Angle.setDegreesAndMinutes: Degree not an integer")
        b_Num = float(b) if '.' in b else int(b)
        if b_Num < 0: 
            raise ValueError("Angle.setDegreesAndMinutes: Minutes must be positive") 
        
        if "." in b:
            if len(b.split('.')[-1]) > 1:
                raise ValueError("Angle.setDegreesAndMinutes: Minutes must only have one decimal point")
        
        if a.isdigit() is False: 
            raise ValueError("Angle.setDegreesAndMinutes:  Degrees must be an integer")
        #if b.isdigit() is False: 
            #raise ValueError("Angle.setDegreesAndMinutes:  Degrees must be an integer")
        if "d" not in degrees: 
            raise ValueError("Angle.setDegreesAndMinutes:  must have separator") 
        if degrees == "": 
            raise ValueError("Angle.setDegreesAndMinutes:  degrees is null string")
        
        pass
        
        
        