## Testing document <br>
Tests can be executed from terminal with the command <br>

>`poetry run invoke test`

### Test coverage
![coverage report](/Documentation/Images/coverage_09.08.PNG) <br>
You can also fetch the coverage from terminal with the command  <br>
>`poetry run invoke coverage`

### Static analysis
You can fetch static analysis information from terminal with the command <br>

>`poetry run invoke lint`

### Unit testing
- Expression parsing (done in the function shunting_yard) is tested in the testing class Testshunting_yard. <br>
- The logical steps of truth table generation (done in the function evaluate in file truth_table.py) is tested in the testing class Testevaluate. The correct truth tables have been generated with WolframAlpha.
- Cosmetic matters of the truth table generation (done in the function create_truth_table in file create_table.py) are left out of testing, since this is not of interest to test.
- Cnf- and dnf-forms are checked in testing classes Testcnf and Testdnf. These have also been checked using WolframAlpha.

### System testing
System testing has been run manually including testing for invalid user inputs. 

### Performance testing
![coverage report](/Documentation/Images/execution_times.png) <br>

Time elapsed has been measured for generating a truth table with number 1-20 of variables using pytest benchmark. This is done in the file truth_table_performance.py. Performance testing can be run with command <br>
>`pytest -v truth_table_performance.py` <br>

from file tests. (This will take a few minutes)

The graph below was generated using pytest benchmark-histogram. <br>
<br>

![coverage report](/Documentation/Images/my_benchmark.svg) <br>
