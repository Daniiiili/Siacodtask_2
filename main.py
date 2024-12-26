from abc import ABC, abstractmethod

class MarioState(ABC):
    @abstractmethod
    def jump(self):
        pass

    @abstractmethod
    def shoot(self):
        pass

    @abstractmethod
    def power_up(self, mario):
        pass

    @abstractmethod
    def power_down(self, mario):
        pass


class NormalState(MarioState):
    def jump(self):
        print("Марио прыгает низко.")

    def shoot(self):
        print("Марио не может стрелять.")

    def power_up(self, mario):
        print("Марио улучшен до улучшенного состояния!")
        mario.set_state(SuperState())

    def power_down(self, mario):
        print("Марио уже в самом слабом состоянии.")


class SuperState(MarioState):
    def jump(self):
        print("Марио прыгает выше.")

    def shoot(self):
        print("Марио не может стрелять.")

    def power_up(self, mario):
        print("Марио улучшен до огненного состояния!")
        mario.set_state(FireState())

    def power_down(self, mario):
        print("Марио вернулся в обычное состояние.")
        mario.set_state(NormalState())


class FireState(MarioState):
    def jump(self):
        print("Марио прыгает очень высоко!")

    def shoot(self):
        print("Марио стреляет огненными шарами!")

    def power_up(self, mario):
        print("Марио уже в самом сильном состоянии.")

    def power_down(self, mario):
        print("Марио вернулся в улучшенное состояние.")
        mario.set_state(SuperState())


class Mario:
    def __init__(self):
        self.state = NormalState()

    def set_state(self, state):
        self.state = state

    def jump(self):
        self.state.jump()

    def shoot(self):
        self.state.shoot()

    def power_up(self):
        self.state.power_up(self)

    def power_down(self):
        self.state.power_down(self)

if __name__ == "__main__":
    mario = Mario()

    mario.jump()
    mario.shoot()
    mario.power_up()

    mario.jump()
    mario.shoot()
    mario.power_up()

    mario.jump()
    mario.shoot()
    mario.power_down()

    mario.jump()
    mario.shoot()
