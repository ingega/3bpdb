from pathlib import Path

# Get the current directory (which is the strategy folder)
current_dir = Path(__file__).resolve().parent

# Reference the parent directory of the current strategy folder
parent_dir = current_dir.parent

# variables and another stuf
entrada=0.6   # ths is the minimum qty of money to use
autoentrada = True
porcentajeentrada = 0.075  #Ojo es 0.0492 en 25x
# pero para que no falle el minimal notional lo ponemos en 6%
leverage = 20
timeframe = 3 #esta variable controla cada cuanto se checan las órdenes
slmax = 0.001  #esta variable controla la pérdida máxima
tp = 0.001
sl = 0.005

path = current_dir
pathGan = str(parent_dir) + "/"
sistema = "3BP "
usuario = " ingega "
bahia = 2
bahias = 3  # este controla el ajuste del saldoO
pausa = 10  # son los segundos que el sistema necesita para no empalmar las lecturas de simula.py
barras = 5   # son los minutos que hacen que el sistema se vaya  a empate
debug_mode = False
# parameters necessary for strategy
# gap=0.03
# distance=0.015
forbidden_hour = 25
bet = 0.005
time = 20  # this is for prevent loops in each4hrs()
a_size = 0.001
b_size = 1
c_size = 0.1
# config for time
hours = 4  # 1 raise zero in preview
minutes = 60
seconds = 40
interval = "1m"
bet_continue = True  # this parameter set the epoch in sl
reverse=False  # in this system doesn't matter because is double bet


def main():
    pass


if __name__ == '__init__':
    main()