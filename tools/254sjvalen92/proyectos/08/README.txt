El programa solo funciona con los archivos BasicLoop, FibonacciSeries y SimpleFunction
Para ejecutar el programa prosiga de la siguiente manera:

python3 VMtranslator.py Directorio.vm

Por ejemplo:
python3 VMtranslator.py FibonacciSeries.vm BasicLoop.vm SimpleFunction.vm

Y obtendra la siguiente salida que corresponde a un array de argumentos y los programas que se traducieron con exito:

['VMtranslator.py', 'FibonacciSeries.vm', 'BasicLoop.vm', 'SimpleFunction.vm']
FibonacciSeries.vm
BasicLoop.vm
SimpleFunction.vm

Los archivos .asm se guardan en su respectivo directorio para verificar haga el comando tree y optendra lo siguiente:

├── BasicLoop
│   ├── BasicLoop.asm
│   ├── BasicLoop.cmp
│   ├── BasicLoop.out
│   ├── BasicLoop.tst
│   ├── BasicLoop.vm
│   └── BasicLoopVME.tst
├── FibonacciSeries
│   ├── FibonacciSeries.asm
│   ├── FibonacciSeries.cmp
│   ├── FibonacciSeries.out
│   ├── FibonacciSeries.tst
│   ├── FibonacciSeries.vm
│   └── FibonacciSeriesVME.tst
├── SimpleFunction
│   ├── SimpleFunction.asm
│   ├── SimpleFunction.cmp
│   ├── SimpleFunction.out
│   ├── SimpleFunction.tst
│   ├── SimpleFunction.vm
│   └── SimpleFunctionVME.tst
└── VMtranslator.py



