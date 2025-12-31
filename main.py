import random


def main():
    rand_num=random.randint(1,100)

    def validate_input(user_guss):
        if not user_guss.isdigit():
            print("try again!")
            return False
        
        user_guss=int(user_guss)
        if user_guss<1 or user_guss>100:
            print("your number should between 1 and 100!")
            return False
        return True



    score =100
    while True:
        user_guss=input("guss number betwin 1 to 100")
        if  user_guss=='q':
            print("goodbye!")
            break
        
        if not validate_input(user_guss):
            continue

        user_guss=int(user_guss)
        if rand_num>user_guss:
            print("your guess is to low")
        elif rand_num<user_guss:
            print("your guess is to high")
        elif rand_num == user_guss:
            print("your guess is to true")
            print("your score is :",score)
            break
        score -=10
        score=max(score,0)


if __name__ =='__main__':
    main()
    