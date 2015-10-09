var mozjpeg = require('imagemin-mozjpeg');
var pngquant = require('imagemin-pngquant');
module.exports = {
    png: {
        options: {
            use: [pngquant({quality: '65-80', speed: 4})]
        },
        files: [{
            expand: true,                       // Enable dynamic expansion
            cwd: "img/",                        // Src matches are relative to this path
            src: ["**/*.png"],                  // Actual patterns to match
            dest: "<%= django.static %>/img/"   // Destination path prefix
        }]
    },
    jpg: {
        options: {
            use: [mozjpeg({quality:80})]
        },
        files: [{
            expand: true,                       // Enable dynamic expansion
            cwd: "img/",                        // Src matches are relative to this path
            src: ["**/*.jpg"],                  // Actual patterns to match
            dest: "<%= django.static %>/img/"   // Destination path prefix
        }]
    }
};
