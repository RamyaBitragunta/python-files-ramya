#name, class, marks in pathology and entomology


class MarksSt:
    def __init__(self,name,section,path,ento):
        self.name = name
        self.section = section
        self.path = path
        self.ento = ento

    def name_sec_path_ento(self):
        print(self.name,"from",self.section,"section","scored",self.path,",",self.ento,"marks in path and ento resp.")

    def printnam(self):
        pass


v1 = MarksSt("Ramya","A",49,48)
v2 = MarksSt("Namya","B",48,47)
v3 = MarksSt("Kavya","A",47,49)
v4 = MarksSt("Divya","B",46,48)

v1.name_sec_path_ento()
v2.name_sec_path_ento()
v3.name_sec_path_ento()
v4.name_sec_path_ento()
