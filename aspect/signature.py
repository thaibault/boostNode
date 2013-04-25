#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-

# region header

'''
    This module provides functions for checking function call's against a
    given signature.
'''
'''
    For conventions see "boostNode/__init__.py" on
    https://github.com/thaibault/boostNode
'''

__author__ = 'Torben Sickert'
__copyright__ = 'see boostNode/__init__.py'
__credits__ = 'Torben Sickert',
__license__ = 'see boostNode/__init__.py'
__maintainer__ = 'Torben Sickert'
__maintainer_email__ = 't.sickert@gmail.com'
__status__ = 'stable'
__version__ = '1.0'

## python2.7 pass
import builtins
import collections
## python2.7 pass
import functools
import inspect
import os
import sys
## python2.7 pass
import types

## python2.7 builtins = sys.modules['__main__'].__builtins__
pass

for number in (3, 4):
    sys.path.append(os.path.abspath(sys.path[0] + number * ('..' + os.sep)))

import boostNode.extension.dependent
import boostNode.extension.native
import boostNode.extension.system
import boostNode.extension.type
import boostNode.paradigm.aspectOrientation

# endregion


# region functions

@boostNode.paradigm.aspectOrientation.JointPoint
## python2.7
## def add_check(point_cut):
def add_check(point_cut: builtins.str) -> builtins.list:
##
    '''
        Adds signature checking in functions and methods for given point cuts.

        Examples:

        >>> add_check(point_cut='^.*test$') # doctest: +ELLIPSIS
        [...]
        >>> @boostNode.paradigm.aspectOrientation.JointPoint
        ... def test():
        ...     pass
    '''
## python2.7
##     pass
    boostNode.paradigm.aspectOrientation.ASPECTS.append(
        {'advice': (
            {'callback': CheckArguments,
             'event': 'call'},
            {'callback': CheckReturnValue,
             'event': 'return'}),
         'point_cut': point_cut})
##
    return boostNode.paradigm.aspectOrientation.ASPECTS

# endregion


# region abstract classes

## python2.7 class CheckObject(builtins.object):
class CheckObject:
    '''
        Checks a function call against a given specification. This class serves
        as helper class.
    '''

    # region dynamic properties

        # region public properties

    '''
        Holds informations about the function and their bounding that is to be
        checked.
    '''
    class_object = object = function = None

        # endregion

        # region protected properties

    '''
        Saves informations in which way the give method is used. It could by
        something like "builtins.staticmethod" or "builtins.classmethod".
    '''
    _method_type = None

        # endregionza

    # endregion

    # region static methods

        # region public methods

            # region special methods

    @boostNode.paradigm.aspectOrientation.JointPoint(builtins.classmethod)
## python2.7
##     def __init__(cls):
    def __init__(cls: boostNode.extension.type.SelfClass) -> None:
##
        '''
            If this method wasn't be overwridden an exception is raised.

            Examples:

            >>> CheckObject() # doctest: +ELLIPSIS
            Traceback (most recent call last):
            ...
            NotImplementedError: Method "__init__" wasn't implemented by "Ob...
        '''
        raise boostNode.extension.native.Object\
            .determine_abstract_method_exception(
                abstract_class_name=CheckObject.__name__)

            # endregion

        # endregion

        # region protected methods

            # region boolean functions

    @builtins.classmethod
## python2.7
##     def _is_multiple_type(cls, type):
    def _is_multiple_type(
        cls: boostNode.extension.type.SelfClass,
        type: (builtins.object, builtins.type)
    ) -> builtins.bool:
##
        '''
            Check wether a given specification allows multiple types.

            Examples:

            >>> CheckObject._is_multiple_type(())
            False

            >>> CheckObject._is_multiple_type(('hans'))
            False

            >>> CheckObject._is_multiple_type(('hans', 5))
            False

            >>> CheckObject._is_multiple_type((str, int))
            True

            >>> CheckObject._is_multiple_type([str, int, bool])
            True

            >>> CheckObject._is_multiple_type((str,))
            False

            >>> CheckObject._is_multiple_type([str])
            False
        '''
        return(
            builtins.isinstance(type, (builtins.tuple, builtins.list)) and
            builtins.len(type) > 1 and
            builtins.isinstance(type[0], builtins.type))

    @builtins.classmethod
## python2.7
##     def _is_right_type(cls, given_type, expected_type):
    def _is_right_type(
        cls: boostNode.extension.type.SelfClass, given_type: builtins.type,
        expected_type: builtins.type
    ) -> builtins.bool:
##
        '''
            Check wether a given type is expected type or given type is a
            subclass of expected type.

            Fixes bug that "bool" is a subtype of "int".

            Examples:

            >>> CheckObject._is_right_type(bool, int)
            False

            >>> CheckObject._is_right_type(list, tuple)
            False

            >>> CheckObject._is_right_type(list, list)
            True

            >>> CheckObject._is_right_type(list, collections.Iterable)
            True
        '''
        return (
            given_type is expected_type or
            builtins.issubclass(given_type, expected_type) and
            not (given_type is builtins.bool and
                 expected_type is builtins.int))

            # endregion

        # endregion

    # endregion

    # region dynamic methods

        # region public methods

            # region special methods

    @boostNode.paradigm.aspectOrientation.JointPoint
## python2.7
##     def __repr__(self):
    def __repr__(self: boostNode.extension.type.Self) -> builtins.str:
##
        '''
            Describes current properties of analysing object.

            Examples:

            >>> def test(self):
            ...     pass
            >>> class A(CheckObject):
            ...     def __init__(self):
            ...         self.function = test
            ...         self._method_type = staticmethod
            >>> repr(A()) # doctest: +ELLIPSIS
            'Object of "A" with class object "None", object "None", called...'
        '''
        class_object_name = 'None'
        if self.class_object is not None:
            class_object_name = self.class_object.__name__
        return ('Object of "{class_name}" with class object "'
                '{class_object_name}", object "{object}", called function '
                '"{function}" and method type "{method_type}".'.format(
                    class_name=self.__class__.__name__,
                    class_object_name=class_object_name,
                    object=builtins.repr(self.object),
                    function=builtins.str(self.function),
                    method_type=builtins.str(self._method_type)))

            # endregion

            # region getter methods

    @boostNode.paradigm.aspectOrientation.JointPoint
## python2.7
##     def get_function_path(self):
    def get_function_path(
        self: boostNode.extension.type.Self
    ) -> builtins.str:
##
        '''
            Returns an object depended function description.

            Examples:

            >>> def test():
            ...     pass
            >>> class A(CheckObject):
            ...     def __init__(self):
            ...         self.function = test
            ...         self._method_type = staticmethod
            >>> a = A()

            >>> a.get_function_path()
            'test'
        '''
## python2.7
##         if self.class_object is not None:
##             return self.class_object.__name__ + '.' + self.function.__name__
##         return self.function.__name__
        return self.function.__qualname__
##

            # endregion

        # endregion

        # region protected methods

## python2.7
##     def _handle_multiple_types(
##         self, value, given_type, expected_types, name='return value'
##     ):
    def _handle_multiple_types(
        self: boostNode.extension.type.Self, value: builtins.object,
        given_type: builtins.type,
        expected_types: (builtins.tuple, builtins.list), name='return value'
    ) -> boostNode.extension.type.Self:
##
        '''
            Check an argument which is specified with multiple types.

            Examples:

            >>> class A(CheckObject):
            ...     def __init__(self):
            ...         pass

            >>> A()._handle_multiple_types(
            ...     'hans', str, (str, int)
            ... ) # doctest: +ELLIPSIS
            Object of "A" with class object "None", object "None", called ...

            >>> a = A()
            >>> a.function = A._handle_multiple_types
            >>> a._handle_multiple_types(
            ...     'hans', str, (bool, int)
            ... ) # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ...
            SignatureError: "_handle_multiple_types()" expects one instance ...

            >>> a._handle_multiple_types(
            ...     'hans', str, [True, 4, 'hans']
            ... ) # doctest: +ELLIPSIS
            Object of "A" with class object "None", object "None", called ...

            >>> a._handle_multiple_types(
            ...     'hans', str, [True, 4, 'peter']
            ... ) # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ...
            SignatureError: "_handle_multiple_types()" expects one value of ...
        '''
        if(builtins.isinstance(expected_types, builtins.tuple) and
           not self._check_again_multiple_types(
               value, given_type, expected_types)):
            raise __exception__(
                '"{function_path}()" expects one instance of '
                '{types} for "{name}" but received "{type_name}".'.format(
                    function_path=self.get_function_path(),
                    types=self._join_types(types=expected_types),
                    name=name, type_name=given_type.__name__))
        elif(builtins.isinstance(expected_types, builtins.list) and
             not value in expected_types):
            raise __exception__(
                '"{function_path}()" expects one value of '
                '{values} for "{name}" but received "{type_name}".'.format(
                    function_path=self.get_function_path(),
                    values=self._join_types(
                        types=expected_types, meta_type=False),
                    name=name, type_name=given_type.__name__))
        return self

## python2.7
##     def _check_type(
##         self, expected_type, given_type, value, name='return value'
##     ):
    def _check_type(
        self: boostNode.extension.type.Self, expected_type: builtins.type,
        given_type: builtins.type, value: builtins.object,
        name='return value'
    ) -> boostNode.extension.type.Self:
##
        '''
            Checks if the given value is of its specified type.

            Examples:

            >>> class A(CheckObject):
            ...     def __init__(self):
            ...         pass
            >>> class B:
            ...     def b(self):
            ...         pass

            >>> A()._check_type(
            ...     builtins.type(None), int, 5
            ... ) # doctest: +ELLIPSIS
            Object of "A" with class object "None", object "None", called ...

            >>> A()._check_type(
            ...     int, int, 5
            ... ) # doctest: +ELLIPSIS
            Object of "A" with class object "None", object "None", called ...

            >>> a = A()
            >>> b = B()
            >>> a.class_object = B
            >>> a.object = b
            >>> a.function = B.b
            >>> a._check_type(
            ...     boostNode.extension.type.Self, B, b
            ... ) # doctest: +ELLIPSIS
            Object of "A" with class object "B", object "...

            >>> a = A()
            >>> a.class_object = B
            >>> a.object = B()
            >>> a.function = B.b
            >>> a._check_type(
            ...     boostNode.extension.type.Self, B, B()
            ... ) # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ...
            SignatureError: "B.b()" expects "... (self)" for "return va..."...

            >>> a = A()
            >>> a.class_object = B
            >>> a.object = B()
            >>> a.function = B.b
            >>> a._check_type(
            ...     boostNode.extension.type.SelfClass, B, B
            ... ) # doctest: +ELLIPSIS
            Object of "A" with class object "B", object "...

            >>> a = A()
            >>> a.class_object = B
            >>> a.object = B()
            >>> a.function = B.b
            >>> a._check_type(
            ...     boostNode.extension.type.SelfClassObject, B, B()
            ... ) # doctest: +ELLIPSIS
            Object of "A" with class object "B", object "...

            >>> a = A()
            >>> a.class_object = B
            >>> a.object = B()
            >>> a.function = B.b
            >>> a._check_type(
            ...     boostNode.extension.type.SelfClassObject, int, 5
            ... ) # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ...
            SignatureError: "B.b()" expects instance of "__main__.B (self c...

            >>> a = A()
            >>> a.class_object = B
            >>> a.object = B()
            >>> a.function = B.b
            >>> a._check_type(
            ...     bool, int, 5
            ... ) # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ...
            SignatureError: "B.b()" expects instance of "bool" for "return ...
        '''
        if not (expected_type is builtins.type(None) or
                expected_type is given_type or
                builtins.issubclass(given_type, expected_type)):
            if expected_type is boostNode.extension.type.Self:
                self._handle_self(name, value)
            elif(expected_type is boostNode.extension.type.SelfClass or
                 expected_type is boostNode.extension.type.SelfClassObject):
                self._handle_self_class(expected_type, given_type, name, value)
            else:
                raise __exception__(
                    '"{function_path}()" expects instance of '
                    '"{object}" for "{name}" but received "{type}" '
                    '({value}).'.format(
                        function_path=self.get_function_path(),
                        object=expected_type.__name__, name=name,
                        type=given_type.__name__, value=builtins.repr(value)))
        return self

## python2.7
##     def _handle_self(self, name, value):
    def _handle_self(
        self: boostNode.extension.type.Self, name: builtins.str,
        value: builtins.object
    ) -> boostNode.extension.type.Self:
##
        '''
            Checks given argument value against the methods bounded object.

            Examples:

            >>> def test():
            ...     pass
            >>> class A(CheckObject):
            ...     def __init__(self):
            ...         self.function = test
            ...         self._method_type = staticmethod
            >>> a = A()

            >>> a._handle_self(
            ...     'argument_name', 'value'
            ... ) # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ...
            boostNode.extension.native.SignatureError: ...instance so "self"...

            >>> a.object = A()
            >>> a._handle_self(
            ...     'argument_name', 'value'
            ... ) # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ...
            boostNode.extension.native.SignatureError:... but received "'val...

            >>> b = A()
            >>> a.object = b
            >>> a._handle_self(
            ...     'argument_name', b
            ... ) # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
            Object of "A" with class object "None", object "Object...
        '''
        if self.object is None:
            raise __exception__(
                '"{function_path}()" wasn\'t called from '
                'an instance so "self" for "{name}" couldn\'t be '
                'determined.'.format(
                    function_path=self.get_function_path(), name=name))
        elif value is not self.object:
            raise __exception__(
                '"{function_path}()" expects "{object} '
                '(self)" for "{name}" but received "{value}".'.format(
                    function_path=self.get_function_path(),
                    object=builtins.repr(self.object), name=name,
                    value=builtins.repr(value)))
        return self

## python2.7
##     def _handle_self_class(self, expected_type, given_type, name, value):
    def _handle_self_class(
        self: boostNode.extension.type.Self,
        expected_type: [boostNode.extension.type.SelfClass,
                        boostNode.extension.type.SelfClassObject],
        given_type: builtins.type, name: builtins.str,
        value: builtins.object
    ) -> boostNode.extension.type.Self:
##
        '''
            Checks given argument value against the methods bounded class.

            Examples:

            >>> def test():
            ...     pass
            >>> class A(CheckObject):
            ...     def __init__(self):
            ...         self.function = test
            ...         self._method_type = staticmethod
            >>> a = A()

            >>> a._handle_self_class(
            ...     boostNode.extension.type.SelfClass, str, 'argument_name',
            ...     'value') # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ...
            boostNode.extension.native.SignatureError:..." wasn't called fr...

            >>> a.class_object = A
            >>> a._handle_self_class(
            ...     boostNode.extension.type.SelfClass, str, 'argument_name',
            ...     'value') # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ...
            boostNode.extension.native.SignatureError: "A.test()" expects ...

            >>> a.class_object = A
            >>> a._handle_self_class(
            ...     boostNode.extension.type.SelfClassObject, str,
            ...     'argument_name', 'value'
            ... ) # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ...
            boostNode.extension.native.SignatureError: "A.test()" expects in...

            >>> a.class_object = A
            >>> a._handle_self_class(
            ...     boostNode.extension.type.SelfClass, A, 'argument_name', A
            ... ) # doctest: +ELLIPSIS
            Object of "A" with class object "A", object "None", called func...

            >>> a.class_object = A
            >>> a._handle_self_class(
            ...     boostNode.extension.type.SelfClassObject, A,
            ...     'argument_name', a) # doctest: +ELLIPSIS
            Object of "A" with class object "A", object "None", called funct...
        '''
        if self.class_object is None:
            raise __exception__(
                '"{function_path}()" wasn\'t called from '
                'a class so "self class" for "{name}" couldn\'t be '
                'determined.'.format(
                    function_path=self.get_function_path(), name=name))
        elif(expected_type is boostNode.extension.type.SelfClass and
             value is not self.class_object):
            raise __exception__(
                '"{function_path}()" expects "{object} '
                '(self class)" for "{name}" but "{type}" ({value}) '
                'received.'.format(
                    function_path=self.get_function_path(),
                    object=self.class_object, name=name,
                    type=given_type.__name__,
                    value=builtins.repr(value)))
        elif(expected_type is
             boostNode.extension.type.SelfClassObject and
             given_type is not self.class_object):
            raise __exception__(
                '"{function_path}()" expects instance of '
                '"{object} (self class)" for "{name}" but "{type}" '
                '({value}) received.'.format(
                    function_path=self.get_function_path(),
                    object=self.class_object, name=name,
                    type=given_type.__name__,
                    value=builtins.repr(value)))
        return self

    @boostNode.paradigm.aspectOrientation.JointPoint
## python2.7
##     def _check_again_multiple_types(
##         self, value, given_type, expected_types
##     ):
    def _check_again_multiple_types(
        self: boostNode.extension.type.Self, value: builtins.object,
        given_type: builtins.type, expected_types: collections.Iterable
    ) -> builtins.bool:
##
        '''
            Checks if given value is one of a set of types.

            Examples:

            >>> class A(CheckObject):
            ...     def __init__(self):
            ...         pass

            >>> A()._check_again_multiple_types(5, int, (int, str))
            True

            >>> A()._check_again_multiple_types(5, int, (bool, str))
            False
        '''
        for expected_type in expected_types:
            if self._is_right_type(given_type, expected_type):
                return True
        return(
            boostNode.extension.type.Self in expected_types and
            value is self.object or
            boostNode.extension.type.SelfClass in expected_types and
            value is self.class_object or
            boostNode.extension.type.SelfClassObject in expected_types and
            given_type is self.class_object)

    @boostNode.paradigm.aspectOrientation.JointPoint
## python2.7
##     def _join_types(self, types, meta_type=True):
    def _join_types(
        self: boostNode.extension.type.Self, types: collections.Sequence,
        meta_type=True
    ) -> builtins.str:
##
        '''
            Join given types for pretty error message presentation.

            Examples:

            >>> class A(CheckObject):
            ...     def __init__(self):
            ...         pass

            >>> A()._join_types((int, str))
            '"int" or "str"'

            >>> A()._join_types((int,))
            '"int"'

            >>> A()._join_types([int, str, bool])
            '"int", "str" or "bool"'

            >>> A()._join_types([int, str, boostNode.extension.type.Self])
            '"int", "str" or "None (self)"'

            >>> a = A()
            >>> a.class_object = A
            >>> a.object = A()
            >>> a._join_types(
            ...     [int, str, boostNode.extension.type.Self]
            ... ) # doctest: +ELLIPSIS
            '"int", "str" or "Object of "A" with class object ...(self)"'

            >>> a = A()
            >>> a.class_object = A
            >>> a.object = A()
            >>> a._join_types(
            ...     [int, str, boostNode.extension.type.SelfClass]
            ... ) # doctest: +ELLIPSIS
            '"int", "str" or "A (self class)"'

            >>> a = A()
            >>> a.class_object = A
            >>> a.object = A()
            >>> a._join_types(
            ...     [int, str, boostNode.extension.type.SelfClassObject]
            ... ) # doctest: +ELLIPSIS
            '"int", "str" or "A (self class object)"'

            >>> a = A()
            >>> a.class_object = A
            >>> a.object = A()
            >>> a._join_types((5, 'hans', a), False) # doctest: +ELLIPSIS
            '"5", "hans" or "Object of "A" with class object "A", ...'

            >>> A()._join_types((5, 'hans', 3), False)
            '"5", "hans" or "3"'

            >>> A()._join_types([5], False)
            '"5"'

            >>> A()._join_types([5, 5], False)
            '"5"'
        '''
        for index, type in builtins.enumerate(types):
            if types.count(type) > 1:
                del types[index]
        if builtins.len(types) < 2:
            return '"' + (
                types[0].__name__ if meta_type else builtins.str(types[0])
            ) + '"'
        return self._join_distinct_types(types, meta_type)

    @boostNode.paradigm.aspectOrientation.JointPoint
## python2.7
##     def _join_distinct_types(self, types, meta_type):
    def _join_distinct_types(
        self: boostNode.extension.type.Self, types: collections.Iterable,
        meta_type: builtins.bool
    ) -> builtins.str:
##
        '''
            Joins a given list of objects to a single human readable string.
        '''
        result = ''
        for type in types:
            if type is boostNode.extension.type.Self:
                result += '"' + builtins.str(self.object) + ' (self)"'
            elif type is boostNode.extension.type.SelfClass:
                result += '"' + self.class_object.__name__ + ' (self class)"'
            elif type is boostNode.extension.type.SelfClassObject:
                result += '"' + self.class_object.__name__ +\
                    ' (self class object)"'
            elif meta_type:
                result += '"' + type.__name__ + '"'
            else:
                result += '"' + builtins.str(type) + '"'
            if type is types[-2]:
                result += ' or '
            elif type is not types[-1]:
                result += ', '
        return result

    @boostNode.paradigm.aspectOrientation.JointPoint
## python2.7
##     def _check_value(self, expected_value, value, name='return value'):
    def _check_value(
        self: boostNode.extension.type.Self,
        expected_value: builtins.object, value: builtins.object,
        name='return value'
    ) -> boostNode.extension.type.Self:
##
        '''
            Checks if the given argument value is equal the specified
            argument value.

            Examples:

            >>> class A(CheckObject):
            ...     def __init__(self):
            ...         pass

            >>> A()._check_value(5, 5) # doctest: +ELLIPSIS
            Object of "A" with class object "None", object "None", ...

            >>> a = A()
            >>> a.function = a._check_value
            >>> a._check_value(
            ...     5, 7
            ... ) # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ...
            SignatureError: "_check_value()" expects value "5" for ... "7".
        '''
        if expected_value != value:
            raise __exception__(
                '"{function_path}()" expects value '
                '"{expected_value}" for "{name}" but received '
                '"{value}".'.format(
                    function_path=self.get_function_path(),
                    expected_value=expected_value, name=name, value=value))
        return self

        # endregion

    # endregion

# endregion


# region classes

class Check(boostNode.paradigm.aspectOrientation.FunctionDecorator):
## python2.7
##     '''
##        This class is needed to be compatiable with future implementations.
##     '''
    '''
        This function provides function and method signature checking.
        An exception is raised on invalid signature implementation.

        There are several possibilities to specify a given argument or
        the return value:

        1. Specify a type.
        2. Specify a number of types via a tuple.
        3. Specify a number of types expected as values explicit via list.
        4. Specify an explicit value.
        5. Specify type implicit by setting a default value.
        6. Specify current instance via "boostNode.extension.type.Self".
        7. Specify any instance of the current class via
           "boostNode.extension.type.SelfClassObject".
        8. Specify the current Class type (interpret as value) for static
           methods via "boostNode.extension.type.SelfClass".

        Examples:

        >>> @Check
        ... def test(num: builtins.int, name: builtins.str) -> tuple:
        ...     return num, name
        >>> test(3, 'hans')
        (3, 'hans')

        >>> test('hans', 'hans') # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        boostNode.extension.native.SignatureError: ..."int" for "num" b...

        >>> @Check
        ... def test() -> builtins.int:
        ...     return 'hans'
        >>> test() # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        boostNode.extension.native.SignatureError: ...int" for "return ...

        >>> @Check
        ... def test(param: 5) -> None:
        ...     variable = param * 2
        >>> test(4) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        boostNode.extension.native.SignatureError: ...m" but received "4".

        >>> @Check
        ... def test(param: (builtins.str, builtins.bool)) -> True:
        ...     return True
        >>> test(True)
        True
        >>> test('hans')
        True
        >>> test(5) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        boostNode.extension.native.SignatureError: ...r" or "bool" for ...

        >>> @Check
        ... def test(param='hans') -> builtins.str:
        ...     return param
        >>> test('peter')
        'peter'
        >>> test('hans')
        'hans'
        >>> test(param='klaus')
        'klaus'
        >>> test(4) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        boostNode.extension.native.SignatureError: ...tr" for "param" b...

        >>> @Check
        ... def test(a='hans', b='and peter') -> builtins.str:
        ...     return a + ' ' + b
        >>> test('klaus')
        'klaus and peter'
        >>> test('hans', 'and fritz')
        'hans and fritz'
        >>> test('peter', b='and hans')
        'peter and hans'
        >>> test(b='and hans')
        'hans and hans'

        >>> @Check
        ... def test() -> None:
        ...     pass
        >>> test('klaus') # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        TypeError: too many positional arguments
        >>> test(b='and hans')
        Traceback (most recent call last):
        ...
        TypeError: too many keyword arguments
        >>> test()

        >>> @Check
        ... def test(*args: builtins.str, **kw: builtins.str) -> None:
        ...     pass
        >>> test('klaus')
        >>> test()
        >>> test('hans', 5) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        boostNode.extension.native.SignatureError: ... for "2. argument" ...
        >>> test('hans', a='peter')
        >>> test(a='peter', b=5) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        boostNode.extension.native.SignatureError: ..."str" for "b" but...

        >>> @Check
        ... def test(*args: (builtins.str, builtins.int)) -> None:
        ...     pass
        >>> test('klaus', 5)
        >>> test(True) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        boostNode.extension.native.SignatureError: ...r" or "int" for "...

        >>> @Check
        ... def test(**kw: (builtins.str, builtins.int)) -> None:
        ...     pass
        >>> test(a='klaus', b=5)
        >>> test(a=True) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        boostNode.extension.native.SignatureError: ...r" or "int" for "...

        >>> @Check
        ... def test(give) -> (builtins.str, builtins.int):
        ...     return give
        >>> test('klaus')
        'klaus'
        >>> test(5)
        5
        >>> test(True) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        boostNode.extension.native.SignatureError: ...r" or "int" for "...

        >>> class test:
        ...     @Check
        ...     def method(self) -> boostNode.extension.type.Self:
        ...         return 5
        >>> test().method() # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        boostNode.extension.native.SignatureError: ...self...turn value...

        >>> class test:
        ...     @Check
        ...     def method(self) -> boostNode.extension.type.Self:
        ...         return self
        >>> test().method() # doctest: +ELLIPSIS
        <...test object at 0x...>

        >>> class test:
        ...     @Check
        ...     def method(self) -> boostNode.extension.type.Self:
        ...         return test()
        >>> test().method() # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        boostNode.extension.native.SignatureError: ...method()" expects...

        >>> class test:
        ...     @Check
        ...     def m(self) -> boostNode.extension.type.SelfClassObject:
        ...         return test()
        >>> test().m() # doctest: +ELLIPSIS
        <...test object at 0x...>

        >>> class test:
        ...     @Check
        ...     def method(self) -> boostNode.extension.type.Self:
        ...         return self
        >>> test().method() # doctest: +ELLIPSIS
        <...test object at 0x...>
    '''
##

    # region dynamic methods

        # region public methods

    @boostNode.paradigm.aspectOrientation.JointPoint
## python2.7
##     def get_wrapper_function(self):
##         '''
##            Dummy method to be compatible to newer features.
##
##            Examples:
##
##            >>> def a(a):
##            ...     return a
##            >>> Check(a).get_wrapper_function() # doctest: +ELLIPSIS
##            <function a at ...>
##
##            >>> Check(a).get_wrapper_function()(5)
##            5
##         '''
##         return self.function
    def get_wrapper_function(
        self: boostNode.extension.type.Self
    ) -> (types.FunctionType, types.MethodType):
        '''
            Returns a wrapper function for the function to be checked.

            Examples:

            >>> def a(a: int):
            ...     return a
            >>> Check(a).get_wrapper_function() # doctest: +ELLIPSIS
            <function a at ...>

            >>> Check(a).get_wrapper_function()(5)
            5

            >>> Check(a).get_wrapper_function()(
            ...     'hans') # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ...
            boostNode.extension.native.SignatureError: "a()" expects inst...
        '''
        @functools.wraps(self.function)
        def wrapper_function(
            *arguments: builtins.object, **keywords: builtins.object
        ) -> builtins.object:
            '''
                Wrapper function for function to be checked.
                Does the argument and return value checks.
                Runs the function to be checked and returns their return
                value.
            '''
            arguments = self._determine_arguments(arguments)
            CheckArguments(
                self.class_object, self.object, self.function, arguments,
                keywords
            ).aspect()
            return_value = self.function(*arguments, **keywords)
            return CheckReturnValue(
                self.class_object, self.object, self.function, arguments,
                keywords, return_value
            ).aspect()
        return wrapper_function
##

        # endregion

    # endregion

## python2.7 """
pass


class CheckArguments(
    boostNode.paradigm.aspectOrientation.CallJointPoint, CheckObject
):
    '''Checks arguments given to a function again their specification.'''

    # region dynamic methods

        # region public methods

## python2.7
##     def aspect(self):
    def aspect(
        self: boostNode.extension.type.Self
    ) -> boostNode.extension.type.Self:
##
        '''
            This function could be used as decorator function or aspects to
            implement argument type check for each function call.

            Examples:

            >>> class A(CheckArguments):
            ...     def __init__(self):
            ...         self.class_object = int
            ...         self.arguments = ()

            >>> a = A()
            >>> a.function = a.aspect
            >>> a.aspect() # doctest: +ELLIPSIS
            Object of "A" with class object "int", object "None", function ...
        '''
        if builtins.hasattr(self.function, '__annotations__'):
            '''
                If there aren't any specifications (signature), the given
                function could be given back unmodified.
            '''
            for argument in self.argument_specifications:
                self._check_argument(argument)
        return self

        # endregion

        # region protected methods

## python2.7
##     def _check_argument_cases(self, argument):
    def _check_argument_cases(
        self: boostNode.extension.type.Self,
        argument: boostNode.paradigm.aspectOrientation.Argument,
    ) -> boostNode.extension.type.Self:
##
        '''
            Handles the different possibilities an argument could be
            specified. It could be specified by a given type, multiple
            types, implicit type through an default value or an explicit
            value.
        '''
        if builtins.isinstance(argument.annotation, builtins.type):
            return self._check_type(
                expected_type=argument.annotation,
                given_type=builtins.type(argument.value),
                value=argument.value, name=argument.name)
        elif self._is_multiple_type(type=argument.annotation):
            return self._handle_multiple_types(
                value=argument.value, given_type=builtins.type(argument.value),
                expected_types=argument.annotation, name=argument.name)
        return self._check_value(
            expected_value=argument.annotation, value=argument.value,
            name=argument.name)

## python2.7
##     def _check_argument(self, argument):
    def _check_argument(
        self: boostNode.extension.type.Self,
        argument: boostNode.paradigm.aspectOrientation.Argument
    ) -> boostNode.extension.type.Self:
##
        '''
            Checks an argument. No matter if argument was given by
            its keyword or not.
        '''
        if argument.default is inspect.Parameter.empty:
            if argument.annotation is not inspect.Parameter.empty:
                self._check_argument_cases(argument)
        else:
            self._check_type(
                expected_type=builtins.type(argument.default),
                given_type=builtins.type(argument.value),
                value=argument.value, name=argument.name)
        return self

        # endregion

    # endregion

## python2.7 """
pass


class CheckReturnValue(
    boostNode.paradigm.aspectOrientation.ReturnJointPoint, CheckObject
):
    '''Checks return value from a function again their specification.'''

    # region dynamic methods

        # region public methods

## python2.7
##     def aspect(self):
    def aspect(self: boostNode.extension.type.Self) -> builtins.object:
##
        '''
            Checks the given return value.

            Returns the original value of the given wrapped function if
            everything goes right.

            Examples:

            >>> class A:
            ...     def __init__(self):
            ...         pass

            >>> CheckReturnValue(
            ...     A, A(), A.__init__, (A(),), {}, return_value='hans'
            ... ).aspect()
            'hans'
        '''
## python2.7
##         pass
        if 'return' in self.function.__annotations__:
            expected_return = self.function.__annotations__['return']
            given_return_type = builtins.type(self.return_value)
            if builtins.isinstance(expected_return, builtins.type):
                self._check_type(
                    given_type=given_return_type,
                    expected_type=expected_return, value=self.return_value)
            elif self._is_multiple_type(type=expected_return):
                self._handle_multiple_types(
                    value=self.return_value, given_type=given_return_type,
                    expected_types=expected_return)
            else:
                self._check_value(
                    expected_value=expected_return, value=self.return_value)
##
        return self.return_value

        # endregion

    # endregion

# endregion

# region footer

boostNode.extension.dependent.Resolve(
    name=__name__, frame=inspect.currentframe(), default_caller=False)

# endregion