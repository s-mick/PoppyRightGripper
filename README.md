# PoppyRightGripper #

Poppy creature based on Poppy Humanoid's right arm, equipped with a two-clamp gripper at wrist level

This robotic device is based on the [Poppy 6-DOF right arm](https://github.com/poppy-project/poppy-6dof-right-arm) by Joel Ortiz. This new prototype was developed during an engineering school six-month internship at [FLOWERS](https://flowers.inria.fr) research team from Inria, in collaboration with [Hybrid](https://u-bordeaux.fr) team from INCIA. This work is part of a project addressing the design of robotic arm prostheses and methods to drive these prostheses with physiological signals. This robotic arm is part of an experimental setup that was elaborated to conduct [usability experiments](https://github.com/s-mick/RobotArmUsability) regarding different control modes that could be used to put a prosthetic arm in motion.

## Properties ##

This Poppy creature is available in two different versions, which are both managed by the same module.
* the `full` version comprises four motors operating the limb and two motors operating the wrist and gripper
* the `noclamp` version comprises only the four motors operating the limb

## Installation ##

Installation requires `setuptools`. Dependencies are the same as the other custom Poppy creatures: [`pypot`](https://github.com/poppy-project/pypot) and [`poppy-creature`](https://github.com/poppy-project/poppy-creature).
Usual ways to set up the modules are:

* Running `python setup.py` requires that the dependencies are already available on the Python version.
* Running `pip install .` in the module's root directory will automatically fetch and install the dependencies.

Depending on the version of `poppy-creature`, this custom Poppy creature may have to be manually "registered" in the `installed_poppy_creatures` dictionary, in `$PYTHON_MODULES/poppy/creatures/__init__.py`.
