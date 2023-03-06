from main import Add

def TestAdd():
        assert Add(2,3) == 5
        assert Add(5,5) == 10
        print("Hàm Add() hoạt động đúng")

if __name__ == '__main__':
        TestAdd()