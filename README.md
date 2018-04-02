# TrAdaBoost

> Wenyuan Dai, Qiang Yang, Gui-Rong Xue, Yong Yu:
[Boosting for transfer learning](http://doi.acm.org/10.1145/1273496.1273521). ICML 2007: 193-200

**Source Code**: http://www.cse.ust.hk/TL/code/C_TraDaBoost.rar

## Instruction

* **OS**: Windows(cmd)
* **Compiler**: g++
* **SVM Classifier**: [SVMLight](http://svmlight.joachims.org/)

## Data

### Format

```
<label> <feature>:<value> <feature>:<value> ... <feature>:<value>
<target> = +1 | -1
<feature> = <integer>
<value> = <float>
```

### Example

* label_pima.tfidf
* unlabel_pima.tfidf

## Run
```
>> test.bat pima 5
```

## NOTE
