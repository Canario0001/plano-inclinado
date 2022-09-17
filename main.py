#!/usr/bin/env python3
from math import sin, cos, radians

def header(num):
        print('┅'*num)

def lista():
        print('\n\nA lista estará da seguinte maneira:\nabreviação: o que significa\nDigite no formato abreviação:valor\n')
        print('p: Força Peso\npx: Força Peso no eixo X\npy: Força Peso no eixo Y (lembrando que é praticamente a mesma coisa que a Normal)')
        print('m: Massa\ng: Gravidade (se não for colocada, será considerada como 10 m/s²)')
        print('a: Aceleração (do objeto)\nfa: Força de atrito\nâ: Ângulo\ncoa: Coeficiente de atrito')

def continha(p, px, py, m, g, a, fa, â, coa):
        err = 'Não foi possível encontrar.'

        if not fa and not coa: # sem atrito
                fa = 0
                coa = 0
                if â:
                        sen = float('{:.3f}'.format(sin(radians(â))))
                        coss = float('{:.3f}'.format(cos(radians(â))))

                if not p:
                        try:
                                p = m*g
                        except (NameError, TypeError): # não tem px ou seno
                                try:
                                        p = px/sen
                                except (NameError, TypeError): # não tem py ou cosseno
                                        try:
                                                p = py/coss
                                        except (NameError, TypeError): p = err

                if not px:
                        try: 
                                px = p * sen
                        except (NameError, TypeError): # não tem p ou seno
                                px = err

                if not py:
                        try:
                                py = p * coss
                        except (NameError, TypeError): # não tem p ou cosseno
                                py = err

                if not m:
                        try:
                                m = p/g
                        except (NameError, TypeError): # não tem p
                                m = err

                if not a:
                        try: 
                                a = px/m
                        except (NameError, TypeError): # não tem px ou m
                                a = err

        else: # com atrito
                if â:
                        sen = float('{:.3f}'.format(sin(radians(â))))
                        coss = float('{:.3f}'.format(cos(radians(â))))

                if not p:
                        try:
                                p = m * g
                        except (NameError, TypeError): # não tem px ou seno
                                try:
                                        p = px/sen
                                except (NameError, TypeError): # não tem py ou cosseno
                                        try:
                                                p = py/coss
                                        except (NameError, TypeError): p = err

                if not px:
                        try: 
                                px = p * sen
                        except (NameError, TypeError): # não tem p ou seno
                                px = err

                if not py:
                        try:
                                py = p * coss
                        except (NameError, TypeError): # não tem p ou cosseno
                                py = err

                if not m:
                        try:
                                m = p/g
                        except (NameError, TypeError): # não tem p
                                m = err

                if not a:
                        try: 
                                a = px/m
                        except (NameError, TypeError): # não tem px ou m
                                a = err

                if not fa:
                        try:
                                fa = coa * py
                        except (NameError, TypeError): # não tem coa ou py
                                try:
                                        fa = - a * m + px
                                except (NameError, TypeError): # não tem a, m ou px
                                        fa = err

                if not coa:
                        try: 
                                coa = fa/py
                        except (NameError, TypeError): # não tem fa ou py
                                coa = err

        result = {
                'p': p,
                'px': px,
                'py': py,
                'm': m,
                'g': g,
                'a': a,
                'fa': fa,
                'â': â,
                'coa': coa
        }
        return result

def main():
        header(35)
        print(' Calculadora de Plano Inclinado!')
        header(35)
        print('\nDeseja começar agora ou ver a lista de abreviações?\n\n[0] - Ver a lista\n[1] - Começar agora\n')
        choice = int(input('>>> '))
        if choice == 0:
                lista()

        elif choice == 1: pass

        else:
                print('Insira uma opção válida. Tente novamente.')
                exit()

        p = None
        px = None
        py = None
        m = None
        g = 10
        a = None
        fa = None
        â = None
        coa = None
        print('\n\nDigite as informações que você possui de acordo com a lista de abreviações. Digite "q" se tiver terminado.\n')
        while True:
                # comp → composto
                comp = input('>>> ').strip().lower()
                if comp == 'q': break
                if comp.startswith('px'):
                        _, px = comp.split(':')
                        px = float(px)

                elif comp.startswith('py'):
                        _, py = comp.split(':')
                        py = float(py)

                elif comp.startswith('p'):
                        _, p = comp.split(':')
                        p = float(p)

                elif comp.startswith('m'):
                        _, m = comp.split(':')
                        m = float(m)

                elif comp.startswith('g'):
                        _, g = comp.split(':')
                        g = float(g)

                elif comp.startswith('a'):
                        _, a = comp.split(':')
                        a = float(a)

                elif comp.startswith('fa'):
                        _, fa = comp.split(':')
                        fa = float(fa)

                elif comp.startswith('â'):
                        _, â = comp.split(':')
                        â = float(â)

                elif comp.startswith('coa'):
                        _, coa = comp.split(':')
                        coa = float(coa)

                else: print('Digite uma informação válida!')

        resultado = continha(p, px, py, m, g, a, fa, â, coa)
        print('\n')
        header(35)
        print('  Resultados')
        header(35)
        print('\n')
        print(f'  Peso: {resultado["p"]} N')
        print(f'  Peso no eixo X: {resultado["px"]} N')
        print(f'  Peso no eixo Y: {resultado["py"]} N')
        print(f'  Massa: {resultado["m"]} kg')
        print(f'  Gravidade: {resultado["g"]} m/s²')
        print(f'  Aceleração: {resultado["a"]} m/s²')
        print(f'  Força de atrito: {resultado["fa"]} N')
        print(f'  Ângulo: {resultado["â"]}°')
        print(f'  Coeficiente de atrito: {resultado["coa"]}')
        print('\n\nObrigado por usar!\nFeito por: Cristian (aka Canário)')


if __name__ == '__main__':
        main()
