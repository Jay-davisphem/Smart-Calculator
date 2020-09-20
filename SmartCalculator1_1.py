

#  SmartCalculator version 1.1
class SmartCalculator1_1:
    
    def __init__(self):
        self.store = {}
        self.help_msg = 'Do all sort of calculations, operations with(out) brackets, \nit support store-use calculation i.e\n'\
        ' \n      >>> a=3\n'\
        '      >>> a + 3\n'\
        '      >>> 6\n'
        self.stop_calc = False
        
    def end_p_m(self, s):
        if s.strip().endswith('-') or s.strip().endswith('+') or s.strip().endswith('/') or s.strip().endswith('*'):
            return True
        return False
    def  command(self, s):
        if s == '/exit':
            print('Bye!')
            self.stop_calc = True
        elif s == '/help':
            print(self.help_msg)
        else:
            print('Unknown command')
    
    def process(self):
        print('SmartCalculator version 1.1\n'\
        'Author: David Oluwafemi Joshua.\n'\
        'About:\n'\
        'A student Python Developer that studies Computer Engineering at\n'\
       'Obafemi Awolowo University, Ile-Ife, Osun State, Nigeria.\n'\
       'Python 3.8.5 ®2020\n')   
        while not self.stop_calc:
            s = input('>>> ')
            if s.startswith('/'):
                self.command(s)
                continue
            if len(s.replace(' ', '')) == 0:
                continue
            self.simplify(s)
    
    def dic_store(self, s):
          i = s.find('=')
          l = s[ :i].strip()
          r = s[i + 1: ].strip()
          self.store[l] = r
    def simplify(self, s):
        if '=' in s:
            l = s[ :s.find('=')].strip()
            if l.isalpha():
                r = s[s.find('=') + 1: ].strip()
                if r.isdigit():
                    self.dic_store(s)
                elif r.isalpha():
                    if r in self.store:
                        self.dic_store(s)
                    else:
                        print('Unknown variable')
                else:
                        if not self.end_p_m(r) and '=' not in r:
                            rs = r.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace(')(', ')*(').replace('*', ' * ').replace('^', ' ** ').replace('/', ' / ')
                            ws = rs.replace('(', '').replace(')', '')
                            for i in ws.split():
                                if (i != '-' or i != '+') and i.isalpha():
                                    rs = rs.replace(i, self.store[i] if self.store[i].isdigit() else self.store[self.store[i]])
                            try:
                                    rs = rs.strip()
                                    if self.end_p_m(rs):
                                        print('Invalid identifier')
                                    else:
                                        self.store[l] = str(eval(rs))
                            except:
                                    print('Invalid assignment')
                        else:
                            print('Invalid assignment')
            else:
               print('Invalid identifier')
        else:
            ss = s.lstrip('+- ')
            if ss.strip().isdigit():
                print(s.replace(' ', ''))
            elif ss.strip().isalpha():
                if ss in self.store:
                    print(self.store[ss] if self.store[ss].isdigit() else self.store[self.store[ss]])
                else:
                    print('Unknown variable')
            else:
                wk = s.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('^', ' ** ').replace('/', ' / ').replace(')(', ')*(')
                wki = wk.replace('(', '').replace(')', '')               
                try:
                    if s.replace(' ', '').isdigit() and not s.isdigit():
                        raise NameError
                    elif s.strip().isalnum() and not s.strip().isalpha():
                        print('Invalid indentifier')                    
                    else:
                        wk = wk.strip()
                        for i in wk.split():
                            if i.isalpha() and i in self.store:
                                wk = wk.replace(i, self.store[i] if self.store[i].isdigit() else self.store[self.store[i]])
                        print(eval(wk))
                except (NameError, SyntaxError):
                    print('Invalid expression')                    
            
sc = SmartCalculator1_1()
sc.process()