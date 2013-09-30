# encoding: utf8
from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [(u'auth', '0001_initial'), (u'app_blog', '0001_initial')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('title', models.CharField(max_length=140, verbose_name=u'\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),), ('body', models.TextField(verbose_name=u'\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430'),), ('date', models.DateField(verbose_name=u'\u0414\u0430\u0442\u0430'),)],
            bases = (models.Model,),
            options = {u'ordering': ('-date',)},
            name = 'blogPost',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('author', models.ForeignKey(to=u'auth.User', to_field=u'id', verbose_name=u'\u0410\u0432\u0442\u043e\u0440 \u043a\u043e\u043c\u0435\u043d\u0442\u0430'),), ('post', models.ForeignKey(to=u'app_blog.blogPost', to_field=u'id', verbose_name=u'\u041f\u043e\u0441\u0442'),), ('comment', ckeditor.fields.RichTextField(verbose_name=u'\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439'),), ('date', models.DateField(verbose_name=u'\u0414\u0430\u0442\u0430'),)],
            bases = (models.Model,),
            options = {},
            name = 'postComment',
        ),
    ]
