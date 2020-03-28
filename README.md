# PyBoltz_Test_Data
The following repository has the data that PyBoltz is ran against. 

## TestData generation
The file "SetupTestSuiteA.py" generates the tests that are put in there. There are three types of tests it can generate. The first one tests the diffusion values and drift velocity values. The second one tests the same values with a magnatic field involved. The third type tests the attachment and ionisation rates.

The file is simple to read. It only puts in the input for PyBoltz, and the expected outputs with errors in a .npy file. This .npy file is then retrieved by PyBotlz, and ran. 

To see how these tests are ran, check the PyBoltz repository.

## Installation
To install this package run the following command.

```
$ sudo pip3 install --upgrade  git+https://github.com/UTA-REST/PyBoltz_Test_Data --user

```
