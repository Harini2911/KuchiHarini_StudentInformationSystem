class DuplicateEnrollmentException(Exception):
    def __init__(self,msg="duplicate enrollment data in the database"):
        self.msg = msg
        super().__init__(self.msg)


class CourseNotFoundException(Exception):
    def __init__(self,msg="Invalid course data in the database"):
        self.msg = msg
        super().__init__(self.msg)


class StudentNotFoundException(Exception):
    def __init__(self,msg="Invalid student data in the database"):
        self.msg = msg
        super().__init__(self.msg)


class TeacherNotFoundException(Exception):
    def __init__(self,msg="Invalid teacher data in the database"):
        self.msg = msg
        super().__init__(self.msg)


class PaymentValidationException(Exception):
    def __init__(self,msg="Invalid payment data in the database"):
        self.msg = msg
        super().__init__(self.msg)


class InvalidDataException(Exception):
    def __init__(self,msg="Invalid choice"):
        self.msg = msg
        super().__init__(self.msg)


class InvalidStudentDataException(Exception):
    def __init__(self,msg="Invalid student data in the database"):
        self.msg = msg
        super().__init__(self.msg)


class InvalidCourseDataException(Exception):
    def __init__(self,msg="Invalid course data in the database"):
        self.msg = msg
        super().__init__(self.msg)


class InvalidEnrollmentDataException(Exception):
    def __init__(self,msg="Invalid enrollment data in the database"):
        self.msg = msg
        super().__init__(self.msg)


class InvalidTeacherDataException(Exception):
    def __init__(self,msg="Invalid teacher data in the database"):
        self.msg = msg
        super().__init__(self.msg)


class InsufficientFundsException(Exception):
    def __init__(self,msg="Insufficient funds in the database"):
        self.msg = msg
        super().__init__(self.msg)
