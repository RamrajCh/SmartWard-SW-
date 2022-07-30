import pickle
from fpdf import FPDF
import nepali_date

today=nepali_date.NepaliDate.today()
today_date=str(today)[3:]
try:
	ward=open("ward.pickle",'rb')
	wardinfo=pickle.load(ward)
	ward.close()
	municipality,address=wardinfo['municipality'],wardinfo['address']
	wardno,state=wardinfo['wardno'],wardinfo['state']
	email,mun_logo=wardinfo['email'] ,wardinfo['mun_logo']
	phone,registrar_name=wardinfo['phone'],wardinfo['registrar_name']
except:
	pass


logo="logo.png"
cOutput="output/certificate.pdf"
rOutput="output/recommendationletter.pdf"
rcpOutput="output/receipt.pdf"

class Certificate():
    def __init__(self):
        #self.logopath=logopath
        self.pdf=FPDF()
        self.pdf.add_page()
        self.addHeader()
        #self.pdf.output(pdffilepath)

    def addLogo(self):
        self.pdf.image(logo,15,30,25,24.67)

    def addHeader(self):
        self.addLogo()
        self.pdf.set_font("Times",size=10)
        self.pdf.cell(180, 8, txt="Schedule-12/13/14/15/16", ln=1, align='C')
        self.pdf.cell(180, 8, txt="(Related with Rule 7)", ln=1, align='C')
        self.pdf.cell(180, 8, txt="Government of Nepal", ln=1, align='C')
        self.pdf.cell(180, 8, txt="Ministry of Federal Affairs and Local Development", ln=1, align='C')
        self.pdf.set_font("Times",'B',size=10)
        self.pdf.cell(180,8,txt="Office Of Local Registrar",ln=1,align='C')
        self.setOfficeAddress(municipality,address)

    def addFooter(self):
        self.pdf.set_font("Times",'B',size=10)
        self.pdf.cell(180, 8, txt="Local Registrar's:", ln=1, align='L')
        self.pdf.set_font("Times",size=10)
        self.pdf.cell(180, 8, txt="Signature:", ln=1, align='L')
        self.pdf.cell(180, 8, txt="Name and Surname: "+registrar_name, ln=1, align='L')
        self.pdf.cell(180,8,txt="Date: "+today_date,ln=1,align='L')

    def setOfficeAddress(self, municipality, address):
        self.pdf.set_font("Times",size=10)
        self.pdf.cell(180,8,txt=municipality,ln=1,align='C')
        self.pdf.cell(180,8,txt=address,ln=1,align="C")

    def getfromtxt(self,txt):
        content=''
        text=open(txt,'r')
        txt=text.readlines()
        return txt

    def output(self):
        self.pdf.output(cOutput)

class BirthCertificate(Certificate):
    def __init__(self):
        super().__init__()
        self.pdf.set_font("Times",'BU',20)
        self.pdf.cell(180,8,txt='Birth Registration Certificate',ln=1,align='C')
        #self.setBody('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #self.getfromtxt('birthcertificate.txt')
        #self.setBody('fdsf')

    def setBody(self,args):
        contents=self.getfromtxt('txtfiles/birthcertificate.txt')
        #args=('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #contents=content.format('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        lines=[]
        for content in contents:
            lines.append(content.format(*args))
        for line in lines:
            self.pdf.set_font('Times',size=10)
            self.pdf.cell(1950,8,txt=line,ln=1,align='L')
        self.addFooter()

class MarriageCertificate(Certificate):
    def __init__(self):
        super().__init__()
        self.pdf.set_font("Times",'BU',20)
        self.pdf.cell(180,8,txt='Marriage Registration Certificate',ln=1,align='C')
        #self.setBody('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #self.getfromtxt('Marriagecertificate.txt')
        #self.setBody('fdsf')

    def setBody(self,args):
        print(args)
        contents=self.getfromtxt('txtfiles/marriagecertificate.txt')
        #args=('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #contents=content.format('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        lines=[]
        for content in contents:
            lines.append(content.format(*args))
        for line in lines:
            self.pdf.set_font('Times',size=10)
            self.pdf.cell(1950,8,txt=line,ln=1,align='L')
        self.addFooter()

class DeathCertificate(Certificate):
    def __init__(self):
        super().__init__()
        self.pdf.set_font("Times",'BU',20)
        self.pdf.cell(180,8,txt='Death Registration Certificate',ln=1,align='C')

    def setBody(self,args):
        contents=self.getfromtxt('txtfiles/deathcertificate.txt')
        lines=[]
        for content in contents:
            lines.append(content.format(*args))
        for line in lines:
            self.pdf.set_font('Times',size=10)
            self.pdf.cell(1950,8,txt=line,ln=1,align='L')
        self.addFooter()

class DivorceCertificate(Certificate):
    def __init__(self):
        super().__init__()
        self.pdf.set_font("Times",'BU',20)
        self.pdf.cell(180,8,txt='Divorce Registration Certificate',ln=1,align='C')

    def setBody(self,args):

        contents=self.getfromtxt('txtfiles/divorcecertificate.txt')
        lines=[]
        for content in contents:
            lines.append(content.format(*args))
        for line in lines:
            self.pdf.set_font('Times',size=10)
            self.pdf.cell(1950,8,txt=line,ln=1,align='L')
        self.addFooter()

class MigrationCertificate(Certificate):
    def __init__(self):
        super().__init__()
        self.pdf.set_font("Times",'BU',20)
        self.pdf.cell(180,8,txt='Migration Registration Certificate',ln=1,align='C')

    def setBody(self,args):
        contents=self.getfromtxt('txtfiles/migrationcertificate.txt')
        lines=[]
        for content in contents:
            lines.append(content.format(*args))
        for line in lines:
            self.pdf.set_font('Times',size=10)
            self.pdf.cell(1950,8,txt=line,ln=1,align='L')

    def setTable(self,data):
        col_width = self.pdf.w / 7.5
        row_height = self.pdf.font_size
        for row in data:
            for item in row:
                self.pdf.cell(col_width, row_height * 1,txt=item, border=1)
            self.pdf.ln(row_height * 1)
        self.addFooter()

class Recommendation():
    def __init__(self):
        self.pdf=FPDF()
        self.pdf.add_page()
        self.addHeader()
        #self.addFooter()
        
    def output(self):
        self.pdf.output(rOutput)

    def addLogo(self):
        self.pdf.image(logo, 5, 5, 12.5*1.5, (24.67*1.5)/2)
        try:
            self.pdf.image(mun_logo,185,5,18.75,18.5625)
        except Exception:
            pass

    def getfromtxt(self,txt):
        text=open(txt,'r')
        txt=text.readlines()
        print (txt)
        return txt

    def addHeader(self):
        self.addLogo()
        self.pdf.set_text_color(255,0,0)
        self.pdf.set_font("Times", size=18)
        self.pdf.cell(180, 6, txt=municipality.title()+" Municipality", ln=1, align='C',)
        self.pdf.set_font("Times", size=14)
        self.pdf.cell(180, 6, txt="Ward No. "+wardno+" Office", ln=1, align='C')
        self.pdf.set_font("Times", size=10)
        self.pdf.cell(180, 6, txt=address, ln=1, align='C')
        self.pdf.cell(180, 6, txt="State No. "+state+", Nepal", ln=1, align='C')
        self.pdf.cell(30,6,txt="Letter No.:",align='L')
        self.pdf.set_x(175)
        self.pdf.cell(30, 6, txt="Date: "+today_date,ln=1,align='L')
        self.pdf.cell(30, 6, txt="Invoice No.:", ln=1, align='L')

        y=self.pdf.get_y()
        self.pdf.set_draw_color(255,0,0)
        self.pdf.set_fill_color(255,0,0)
        self.pdf.rect(0,y+2,220,.75,'DF')

    def setRegistrar(self):
        y = self.pdf.get_y()
        self.pdf.set_y(y+20)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.set_font("Times", 'B', size=10)
        self.pdf.cell(180, 8, txt="Verified By:", ln=1, align='L')
        self.pdf.set_font("Times", size=10)
        self.pdf.cell(180, 8, txt="Signature:", ln=1, align='L')
        self.pdf.cell(180, 8, txt="Name and Surname: " + registrar_name, ln=1, align='L')
        self.pdf.cell(180, 8, txt="Date: " + today_date, ln=1, align='L')
        self.addFooter()

    def setTable(self,data):
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_fill_color(0, 0, 0)
        col_width = self.pdf.w / 5.5
        row_height = self.pdf.font_size
        for row in data:
            for item in row:
                self.pdf.cell(col_width, row_height * 1,txt=item, border=1)
            self.pdf.ln(row_height * 1)

    def addFooter(self):
        self.pdf.set_y(-28)
        self.pdf.set_text_color(255, 0, 0)
        self.pdf.set_font('Times', '', 8)
        self.pdf.cell(0, 5,"Email: "+email+", Phone No.: "+phone, ln=1, align='C')

class IncomeReco(Recommendation):
    def __init__(self):
        super().__init__()

    def setBody(self, args):
        self.pdf.set_text_color(0, 0, 0)
        y=self.pdf.get_y()
        self.pdf.set_y(y+5)
        self.pdf.set_font("Times", size=10)
        self.pdf.cell(180, 8, txt="Subject:Source of Income", ln=1, align='L')
        self.pdf.cell(180, 8, txt="To whom it may concern", ln=1, align='L')
        text='This is to certify that Mr. {0},son of {1}, permanent resident of'.format(*args)
        self.pdf.cell(180, 8, txt=text, ln=1, align='L')
        text ='ward no. {2}, {3} municipality has a following annual income of different sources as shown below.'.format(*args)
        self.pdf.cell(180, 8, txt=text, ln=1, align='L')

    def setTotalIncome(self,data):
        self.pdf.cell(180, 8, txt="", ln=1, align='L')
        self.pdf.set_font("Times",'BU', size=10)
        self.pdf.cell(180, 8, txt="Total Income:", ln=1, align='L')
        self.pdf.cell(180, 8, txt="In Figure: "+str(data[0]), ln=1, align='L')
        self.pdf.cell(180, 8, txt="In Words: Rs. "+data[1].title()+" Only.", ln=1, align='L')
        self.setRegistrar()

class GharBatoReco(Recommendation):
    def __init__(self):
        super().__init__()

    def setBody(self, args):
        self.pdf.set_text_color(0, 0, 0)
        y=self.pdf.get_y()
        self.pdf.set_y(y+5)
        self.pdf.set_font("Times", size=10)
        self.pdf.cell(180, 8, txt="Subject: Verification of road network", ln=1, align='FJ')
        self.pdf.cell(180, 8, txt="", ln=1, align='L')
        self.pdf.cell(180, 8, txt="Revenue office,{3},".format(*args), ln=1, align='FJ')
        self.pdf.cell(180, 8, txt="", ln=1, align='L')
        text='In relation to above, this is to verify that Mr./Mrs. {0}, having permanent address'.format(*args)
        self.pdf.cell(180, 8, txt=text, ln=1, align='FJ')
        text ='{1} with citizenship certificate number {2} has access to road network for following property of '.format(*args)
        self.pdf.cell(180, 8, txt=text, ln=1, align='FJ')
        text = 'him/her situated in this ward.'.format(*args)
        self.pdf.cell(180, 8, txt=text, ln=1, align='FJ')

class TypeRecommendation(Recommendation):
    def setSubject(self,subject):
        self.pdf.set_text_color(0, 0, 0)
        y = self.pdf.get_y()
        self.pdf.set_y(y + 5)
        self.pdf.set_font('Times', 'BU',size=10)
        self.pdf.cell(1950, 8, txt="Subject: "+subject, ln=1, align='L')

    def setBody(self):
        self.pdf.set_text_color(0, 0, 0)
        lines = self.getfromtxt('txtfiles/newrecommendation.txt')
        for line in lines:
            self.pdf.set_font('Times', size=10)
            self.pdf.cell(1950, 8, txt=line, ln=1, align='L')
        self.setRegistrar()

class Receipt():
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.addHeader()

    def addHeader(self):
        self.pdf.set_text_color(255, 0, 0)
        self.pdf.set_font("Times", size=18)
        self.pdf.cell(180, 6, txt=municipality.title() + " Municipality", ln=1,align='C')
        self.pdf.set_font("Times", size=14)
        self.pdf.cell(180, 6, txt="Ward No. "+wardno+" Office", ln=1, align='C')
        self.pdf.set_font("Times", size=10)
        self.pdf.cell(180, 6, txt=address, ln=1, align='C')
        self.pdf.cell(180, 6, txt="State No. "+state+", Nepal", ln=1, align='C')

    def setBody(self,data):
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.set_font("Times",'B',size=10)
        self.pdf.cell(180, 6, txt="Receipt No.: "+data[0][0],align='L')
        self.pdf.set_x(175)
        self.pdf.cell(30, 6, txt="Date: " + today_date, ln=1, align='L')
        self.pdf.cell(180, 6, txt="Name: " + data[0][1], ln=1, align='L')
        self.setTable(data[1])
        self.setIncome(data[0][2])
        self.setRegistrar()

    def setTable(self,data):
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_fill_color(0, 0, 0)
        col_width = self.pdf.w / 5
        row_height = self.pdf.font_size
        for row in data:
            for item in row:
                self.pdf.cell(col_width, row_height * 1,txt=item, border=1)
            self.pdf.ln(row_height * 1)

    def setIncome(self,data):
        self.pdf.cell(180, 8, txt="", ln=1, align='L')
        self.pdf.set_font("Times", 'BU', size=10)
        self.pdf.cell(180, 8, txt="Total Income:", ln=1, align='L')
        self.pdf.cell(180, 8, txt="In Figure: " + str(data[0]), ln=1, align='L')
        self.pdf.cell(180, 8, txt="In Words: Rs. " + data[1].title() + " Only.", ln=1, align='L')

    def setRegistrar(self):
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.set_font("Times", 'B', size=10)
        self.pdf.cell(180, 8, txt="Received By:", ln=1, align='L')
        self.pdf.set_font("Times", size=10)
        self.pdf.cell(180, 8, txt="Signature:", ln=1, align='L')
        self.pdf.cell(180, 8, txt="Name and Surname: " + registrar_name, ln=1, align='L')
        self.pdf.cell(180, 8, txt="Date: " + today_date, ln=1, align='L')

    def output(self):
        self.pdf.output(rcpOutput)
