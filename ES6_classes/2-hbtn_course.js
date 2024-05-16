export default class HolbertonCourse {
    constructor(name, length, students) {
        if (typeof (name) === 'string') {
            this._name = name;
        } else {
            throw new TypeError('Name must be a string')
        }

        if (typeof (length) === 'number') {
            this._length = length;
        } else {
            throw new TypeError('Length must be a number')
        }

        if (Array.isArray(students) && students.every((s) => typeof s === 'string')) {
            this._students = students;
        } else {
            throw new TypeError('Students must be a array of strings')
        }
    }

    get name() {
        return this._name;
    }

    set name(name) {
        this._name = name;
    }

    get length() {
        return this._length;
    }

    set length(length) {
        this._length = length;
    }

    get students() {
        return this._students;
    }

    set students(students) {
        this._students = students;
    }
}