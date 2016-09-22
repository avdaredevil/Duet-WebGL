"use strict";
const gulp = require('gulp');
const pug = require('pug');
const vulcanize = require('gulp-vulcanize');
const rename = require('gulp-rename');
const $ = require('gulp-load-plugins')();
const runSequence = require('run-sequence');
const merge = require('merge-stream');
const minifyInline = require('gulp-minify-inline')
const path = require('path');
const clean = require('gulp-clean');
 
const DIST = 'package';
var dist = function(subpath) {
    return !subpath?DIST:path.join(DIST, subpath);
};
//=====================================================|
var imageOptimizeTask = function(src, dest) {
  return gulp.src(src)
    .pipe($.imagemin({
      progressive: true,
      interlaced: true
    }))
    .pipe(gulp.dest(dest))
    .pipe($.size({title: 'images'}));
};
var optimizeHtmlTask = function(src, dest) {
  return gulp.src(src)
    // Concatenate and minify JavaScript
    .pipe($.if('*.js', $.uglify({preserveComments: 'none'})))
    // Concatenate and minify styles
    // In case you are still using useref build blocks
    .pipe($.if('*.css', $.cleanCss()))
    // Minify any HTML
    .pipe($.if('*.html', $.minifyHtml({
      quotes: true,
      empty: true,
      spare: true
    })))
    // Output files
    .pipe(gulp.dest(dest))
    .pipe($.size({
      title: 'html'
    }));
};
//=====================================================|
gulp.task('copy', function() {
    var app = gulp.src([
        'app/**/*',
        '!app/bower_components',
        '!app/*.pug',
        '!app/elements.html',
    ], {
        dot: true
    }).pipe($.changed(dist('bower_components'))).pipe(gulp.dest(dist()));

    // Copy over only the bower_components we need
    // These are things which cannot be vulcanized
    var bower = gulp.src([
        'app/bower_components/{webcomponentsjs,promise-polyfill,trianglify,moment}/**/*'
    ]).pipe($.changed(dist('bower_components'))).pipe(gulp.dest(dist('bower_components')));

    return merge(app, bower)
        .pipe($.size({
            title: 'copy'
        }));
});
gulp.task('images', function() {return imageOptimizeTask(['app/public/**/*.png','app/public/**/*.ico','app/public/**/*.jpg'], dist('public'))});
gulp.task('html', function() {return optimizeHtmlTask(
    ['app/*.html','!app/elements.html', dist("main.html")],
    dist())
});
gulp.task('pug', function() {
    return gulp.src(["app/*.pug"])
        .pipe($.pug())
        .pipe(gulp.dest(dist()))
})
gulp.task('vulcanize', function() {
    return gulp.src('app/elements.html')
        .pipe(gulp.dest('app/bower_components'))
        .pipe($.vulcanize({
            stripComments: true,
            inlineCss: true,
            inlineScripts: true
        }))
        .pipe($.if('*.html', $.minifyHtml({
            quotes: true,
            empty: true,
            spare: true
        })))
        .pipe(minifyInline())
        .pipe(gulp.dest(dist()))
        .pipe($.size({title: 'vulcanize'}));
});
//=====================================================|
gulp.task('watch', ()=>{
    gulp.watch("app/*.pug", 'pug');
})
gulp.task('clean', ()=>{
	return gulp.src(['app/bower_components/elements.*',dist("elements.html")], {read: false})
		.pipe(clean());
})
//=====================================================|
gulp.task('default', ['clean'], function(cb) {
    runSequence(
        'copy',
        ['pug','images', 'vulcanize'],
        'html', 'watch',
    cb);
});