class Car:
    def init(self, model, color, speed=0):
        """
        Initializes a new Car object.

        Args:
            model (str): موديل السيارة
            color (str): لون السيارة
            speed (int, optional): سرعة السيارة. Defaults to 0.
        """
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self):
        """
        زيادة السرعة
        """
        self.speed += 10
        print(f"سرعة السيارة: {self.speed} كم/ساعة")

    def brake(self):
        """
        تقليل السرعة
        """
        if self.speed > 0:
            self.speed -= 10
            print(f"سرعة السيارة: {self.speed} كم/ساعة")
        else:
            print("السرعة уже صفر")

    def show_info(self):
        """
        عرض معلومات السيارة
        """
        print(f"موديل السيارة: {self.model}")
        print(f"لون السيارة: {self.color}")
        print(f"سرعة السيارة: {self.speed} كم/ساعة")

# إنشاء سيارة جديدة
my_car = Car("Toyota", "أبيض")

# عرض معلومات السيارة
my_car.show_info()

# زيادة السرعة
my_car.accelerate()
my_car.accelerate()

# تقليل السرعة
my_car.brake()
my_car.brake()