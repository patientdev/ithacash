module.exports = function(grunt) {

  var django = {
    static: '../../ithacash_dev/static'
  };

  // Project config
  grunt.initConfig({
    django: django,
    pkg: grunt.file.readJSON('package.json'),
    // uglify: {
    //   options: {
    //     banner: '/*! <%= pkg.name %>.js <%= grunt.template.today("yyyy-mm-dd") %> */\n'
    //   },
    //   global: {
    //     files: {
    //       '<%= globalConfig.src  %>/js/patient.js': ['js/patient.dev.js']
    //     }
    //   }
    // },

    sass: {
      global: {
        options: {
          style: "compressed"
        },
        files: {
          "<%= django.static %>/style-guide/css/style-guide.css": "<%= django.static %>/style-guide/css/style-guide.scss"
        }
      }
    },

    watch: {
      options: {
        livereload: true
      },
      css: {
        files: ["<%= django.static %>/style-guide/css/style-guide.scss"],
        tasks: ["sass"]
      }
    }

    // autoprefixer: {
    //   global: {
    //     src: "temp/global-unprefixed.dev.css",
    //     dest: "<%= globalConfig.src  %>/css/ithacash.css"
    //   }
    // },

    // jshint: {
    //   options: {
    //     reporter: require('jshint-stylish')
    //   },
    //   files: {
    //     src: ['js/ithacash.dev.js']
    //   }
    // },

    // csslint: {
    //   src: ['<%= globalConfig.src  %>/css/ithacash.css']
    // },

    // scsslint: {
    //   allFiles: [
    //     'scss/*.scss',
    //   ],
    //   options: {
    //     compact: true
    //   }
    // }

  });

  require("load-grunt-tasks")(grunt);

  // Tasks
  grunt.registerTask("test", ["jshint", "scsslint", "csslint"]);
  grunt.registerTask("build", ["uglify", "sass", "autoprefixer"]);
  grunt.registerTask("scss", ["sass"]);
  grunt.registerTask("dev", ["sass", "watch"]);
  grunt.registerTask("default", "Let's get 'er going here now", function() {
    grunt.task.run('test', 'build');
  })
};