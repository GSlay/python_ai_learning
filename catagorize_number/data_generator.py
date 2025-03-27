import random

class data_generator:
    def __init__(self, pivot:int, num_data:int):
        self.pivot:int = pivot
        self.num_data:int = num_data
        self._inputs:list[int] = []
        self._labels:list[int] = []
        self._generate_data()

    def _generate_data(self):
        for _ in range(self.num_data):
            # Tạo số ngẫu nhiên có thể lớn hơn hoặc bé hơn pivot
            random_offset = random.randint(-self.pivot - 10, self.pivot + 10) # Phạm vi có thể điều chỉnh
            random_number = self.pivot + random_offset
            self._inputs.append(random_number)
            self._labels.append(random_number > self.pivot)

    def show_data(self):
        print("Dữ liệu đã tạo:")
        for i in range(self.num_data):
            print(f"Input: {self._inputs[i]}, Label: {self._labels[i]}")

if __name__ == '__main__':
    # Ví dụ sử dụng class
    pivot_value = 50
    number_of_data = 10
    data_gen = data_generator(pivot=pivot_value, num_data=number_of_data)
    data_gen.show_data()
