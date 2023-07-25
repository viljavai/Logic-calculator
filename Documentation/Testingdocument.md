## Testing document <br>
Tests can be executed from terminal with the command <br>

>`poetry run invoke test`

### Test coverage
Test coverage can be found in html-format [here.](/htmlcov/index.html) <br>
You can also fetch the coverage from terminal with the command  <br>
>`poetry run invoke coverage`

### Static analysis
You can fetch static analysis information from terminal with the command <br>

>`poetry run invoke lint`

### Unit testing
- Expression parsing (done in the function shunting_yard) is tested in the testing class Testshunting_yard. <br>
- The logical steps of truth table generation (done in the function evaluate) is tested in the testing class Testevaluate.

### System testing
System testing has been run manually.