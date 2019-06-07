# Generated by Django 2.2.1 on 2019-06-06 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField()),
            ],
            options={
                'db_table': 'content',
                'ordering': ['sequence'],
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'course_resource',
            },
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klazor.Folder')),
            ],
            options={
                'db_table': 'folder',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('link', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'instructor',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('folder', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='klazor.Folder')),
            ],
            options={
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='AudioContent',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Content')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('audio', models.FileField(upload_to='audios')),
            ],
            options={
                'db_table': 'audio_content',
            },
            bases=('klazor.content',),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Item')),
                ('category_set', models.ManyToManyField(blank=True, to='klazor.Category')),
                ('instructor_set', models.ManyToManyField(blank=True, to='klazor.Instructor')),
                ('resource_set', models.ManyToManyField(blank=True, to='klazor.CourseResource')),
            ],
            options={
                'db_table': 'course',
            },
            bases=('klazor.item',),
        ),
        migrations.CreateModel(
            name='FileCourseResource',
            fields=[
                ('courseresource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.CourseResource')),
                ('file', models.FileField(upload_to='resources/files')),
            ],
            options={
                'db_table': 'file_course_resource',
            },
            bases=('klazor.courseresource',),
        ),
        migrations.CreateModel(
            name='ImageContent',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Content')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.FileField(upload_to='images')),
                ('scale', models.FloatField(default=1)),
            ],
            options={
                'db_table': 'image_content',
            },
            bases=('klazor.content',),
        ),
        migrations.CreateModel(
            name='LinkCourseResource',
            fields=[
                ('courseresource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.CourseResource')),
                ('link', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'link_course_resource',
            },
            bases=('klazor.courseresource',),
        ),
        migrations.CreateModel(
            name='MarkdownContent',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Content')),
                ('text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'markdown_content',
            },
            bases=('klazor.content',),
        ),
        migrations.CreateModel(
            name='NotSchool',
            fields=[
                ('instructor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Instructor')),
            ],
            options={
                'db_table': 'not_school',
            },
            bases=('klazor.instructor',),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('instructor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Instructor')),
                ('admissions_link', models.TextField(blank=True, null=True)),
                ('programs_link', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'school',
            },
            bases=('klazor.instructor',),
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Item')),
            ],
            options={
                'db_table': 'sheet',
            },
            bases=('klazor.item',),
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Content')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('video', models.FileField(upload_to='videos')),
                ('scale', models.FloatField(default=1)),
            ],
            options={
                'db_table': 'video_content',
            },
            bases=('klazor.content',),
        ),
        migrations.CreateModel(
            name='CourseItem',
            fields=[
                ('sheet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Sheet')),
                ('completed', models.BooleanField(default=False)),
                ('sequence', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'course_item',
                'ordering': ['sequence'],
            },
            bases=('klazor.sheet',),
        ),
        migrations.CreateModel(
            name='MoocCourse',
            fields=[
                ('course_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Course')),
            ],
            options={
                'db_table': 'mooc_course',
            },
            bases=('klazor.course',),
        ),
        migrations.AddField(
            model_name='content',
            name='sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klazor.Sheet'),
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('item_set', models.ManyToManyField(to='klazor.CourseItem')),
                ('mooc_course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='klazor.MoocCourse')),
            ],
            options={
                'db_table': 'week',
            },
        ),
        migrations.CreateModel(
            name='SchoolCourse',
            fields=[
                ('course_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Course')),
                ('year', models.SmallIntegerField(blank=True, null=True)),
                ('semester', models.SmallIntegerField(blank=True, null=True)),
                ('item_set', models.ManyToManyField(to='klazor.CourseItem')),
            ],
            options={
                'db_table': 'school_course',
            },
            bases=('klazor.course',),
        ),
    ]
