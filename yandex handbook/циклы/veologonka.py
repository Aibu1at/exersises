"""По правилам велогонки, после квалификации каждый гонщик стартует с задержкой на секунду больше, чем у гонщика перед ним.
Первый гонщик стартует на счёт 3. Напишите программу, которая сможет автоматизировать старт всех гонщиков, участвующих в велогонке."""

n = int(input())
countdown = 3
for gonshik in range(n):
    for i in range(countdown, 0, -1):
        print(f'До старта {i} секунд(ы)')
    print(f'Старт {gonshik + 1}!!!')
    countdown += 1