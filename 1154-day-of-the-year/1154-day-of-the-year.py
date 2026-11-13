class Solution:
    def dayOfYear(self, date: str) -> int:
        m = {
            "01":0,
            "02": 31, 
            "03": 59,
            "04": 90, 
            "05": 120,
            "06": 151, 
            "07": 181,
            "08": 212, 
            "09": 243,
            "10": 273, 
            "11": 304,
            "12": 334,
            }
        extrafeb=0
        if(int(date[5:7]))>2:
            if int(date[0:4]) % 400 == 0 or (int(date[0:4])  % 4 == 0 and int(date[0:4])  % 100 != 0):
                extrafeb=1
        
        return m[date[5:7]]+int(date[8:10])+extrafeb