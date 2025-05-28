from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Renderiza o index.html que estende modelo.html
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operacao = request.form['operacao']
            resultado = None

            if operacao == 'soma':
                resultado = num1 + num2
            elif operacao == 'subtracao':
                resultado = num1 - num2
            elif operacao == 'multiplicacao':
                resultado = num1 * num2
            elif operacao == 'divisao':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = "Erro: Divisão por zero!"
            else:
                resultado = "Operação inválida."

            # Passa o resultado para o template index.html
            return render_template('index.html', resultado=resultado)
        except ValueError:
            return render_template('index.html', resultado="Erro: Entrada inválida. Por favor, insira números.")
        except Exception as e:
            return render_template('index.html', resultado=f"Ocorreu um erro: {e}")

if __name__ == '__main__':
    app.run(debug=True)