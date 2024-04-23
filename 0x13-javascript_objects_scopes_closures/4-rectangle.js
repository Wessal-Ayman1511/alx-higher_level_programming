#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const var1 = this.height;
    const var2 = this.width;
    this.width = var1;
    this.hight = var2;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
