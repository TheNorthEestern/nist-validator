class NISTRules:

    def __init__(self):
        self.min_password_length = 8
        self.max_password_length = 64

    def password_is_too_short(self, password):
        return len(password) < self.min_password_length

    def password_is_too_long(self, password):
        return len(password) > self.max_password_length

    def is_ascii(self, password):
        return len(password) == len(password.encode())

    def is_common(self, password, password_list):
        return password in password_list

class NISTValidator(NISTRules):
    
    def __init__(self, input_stream=[], password_list=set()):
        super().__init__()
        self.input_stream = input_stream
        self.password_list = set(password_list)

    def validation_error(self, offender, reason):
        print("Error: %s -> %s" % (reason, offender))

    def validate(self):
        for password in self.input_stream:
            if not self.is_ascii(password):
                self.validation_error(password, "Password Contains Invalid Characters")
            elif self.password_is_too_short(password):
                self.validation_error(password, "Too Short")
            elif self.password_is_too_long(password):
                self.validation_error(password, "Too Long")
            elif self.is_common(password, self.password_list):
                self.validation_error(password, "Too Common")
