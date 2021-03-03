from PyQt5 import  uic,QtWidgets

def funcao_principal():
    linha1 = projeto.lineEdit.text()
    linha2 = projeto.lineEdit_2.text()
    linha3 = projeto.lineEdit_3.text()

    if projeto.radioButton.isChecked() :
        print("Categoria Monitor selecionada") 
    elif projeto.radioButton_2.isChecked() :
        print("Categoria Mouse selecionada")
    elif projeto.radioButton_3.isChecked() :
        print("Categoria Teclado selecionada")
    elif projeto.radioButton_4.isChecked() :
        print("Categoria Impressora selecionada")
    elif projeto.radioButton_5.isChecked() :
        print("Categoria Roteador selecionada")
    elif projeto.radioButton_6.isChecked() :
        print("Categoria Gabinete selecionada")
    elif projeto.radioButton_7.isChecked() :
        print("Categoria Cabos em geral selecionada")
    elif projeto.radioButton_8.isChecked() :
        print("Categoria Caixa de som/headset selecionada")
    elif projeto.radioButton_9.isChecked() :
        print("Categoria Nobreak/Estabilizador selecionada")
    else :
        print("Categoria Outros selecianada")
        
    print("Data de recebimento:",linha1)
    print("Descricao:",linha2)
    print("Código ",linha3)

    projeto.lineEdit.setText("")
    projeto.lineEdit_2.setText("")
    projeto.lineEdit_3.setText("")

app=QtWidgets.QApplication([])
projeto=uic.loadUi("projeto.ui")
projeto.pushButton.clicked.connect(funcao_principal)

projeto.show()
app.exec()