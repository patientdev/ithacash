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
          "temp/style-guide.css": "scss/main.scss"
        }
      }
    },

    watch: {
      options: {
        livereload: true
      },
      css: {
        files: ["scss/*.scss", "<%= django.static %>/../../templates/style-guide.html"],
        tasks: ["sass", "csslint"]
      }
    },

    autoprefixer: {
      global: {
        src: "temp/style-guide.css",
        dest: "<%= django.static %>/style-guide/css/style-guide.css"
      }
    },

    // jshint: {
    //   options: {
    //     reporter: require('jshint-stylish')
    //   },
    //   files: {
    //     src: ['js/ithacash.dev.js']
    //   }
    // },

    csslint: {
      src: ['<%= django.static %>/style-guide/css/style-guide.css'],
      options: {
        format: 'compact'
      }
    },

    scsslint: {
      allFiles: [
        'scss/*.scss',
      ],
      options: {
        compact: true
      }
    }

  });

  require("load-grunt-tasks")(grunt);

  // Tasks
  grunt.registerTask("test", ["jshint", "scsslint", "csslint"]);
  grunt.registerTask("build", ["uglify", "sass", "autoprefixer"]);
  grunt.registerTask("scss", ["sass"]);
  grunt.registerTask("dev", ["sass", "autoprefixer", "csslint", "watch"]);
  grunt.registerTask("default", "Let's get 'er going here now", function() {
    grunt.task.run('test', 'build');
  })
};