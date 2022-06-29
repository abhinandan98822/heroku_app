# Generated by Django 3.2.12 on 2022-05-11 12:48

import dashboard.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.CharField(choices=[('AD', 'AD'), ('BT', 'BT'), ('OT', 'OT'), ('ST', 'ST'), ('PT', 'PT'), ('SE', 'SE'), ('FO', 'FO')], max_length=2)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('theropy', models.CharField(max_length=100)),
                ('signature', models.FileField(blank=True, upload_to='signature')),
                ('password', models.CharField(max_length=120)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(null=True)),
                ('created_on', models.DateField(auto_now=True)),
                ('created_by', models.CharField(max_length=200)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', dashboard.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ClientTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6)),
                ('dob', models.DateField(blank=True, null=True)),
                ('month', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, default='123456789', max_length=12, null=True)),
                ('alternate_phone', models.CharField(blank=True, default='123456789', max_length=12, null=True)),
                ('mother_tongue', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('mother_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('branch', models.CharField(max_length=200)),
                ('created_on', models.DateField()),
                ('created_by', models.CharField(max_length=200)),
                ('modified_on', models.DateTimeField(blank=True, null=True)),
                ('modified_by', models.CharField(max_length=200)),
                ('discontinious', models.CharField(default='False', max_length=8)),
                ('discontinious_on', models.DateField(blank=True, null=True)),
                ('assessment', multiselectfield.db.fields.MultiSelectField(choices=[('BT', 'BT'), ('OT', 'OT'), ('ST', 'ST')], max_length=10)),
                ('slot_time_from', models.TimeField(blank=True, null=True)),
                ('slot_time_to', models.TimeField(blank=True, null=True)),
                ('theropy', models.CharField(choices=[('Integrated', 'Integrated'), ('Individual', 'Individual')], max_length=100)),
                ('theropyselect', multiselectfield.db.fields.MultiSelectField(choices=[('BT', 'BT'), ('OT', 'OT'), ('ST', 'ST'), ('PT', 'PT'), ('SE', 'SE')], max_length=100)),
                ('chief_complaints', models.TextField()),
                ('diagnosis', models.TextField()),
                ('remarks', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='STAssesment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('therapist', models.CharField(max_length=100)),
                ('date_of_assessment', models.DateField()),
                ('babbling', models.TextField()),
                ('first_word', models.TextField()),
                ('main_mode_comm', models.TextField()),
                ('family_history', models.TextField()),
                ('motor_developments', models.TextField()),
                ('oro_peripheral_mechanism', models.TextField()),
                ('vegetative_skills', models.TextField()),
                ('vision', models.TextField()),
                ('hearing', models.TextField()),
                ('response_to_name_call', models.TextField()),
                ('environmental_sounds', models.TextField()),
                ('eye_contact', models.TextField()),
                ('attention_to_sound', models.TextField()),
                ('imitation_to_body_movements', models.TextField()),
                ('imitation_to_speech', models.TextField()),
                ('attention_level', models.TextField()),
                ('social_smile', models.TextField()),
                ('initiates_interaction', models.TextField()),
                ('receptive_language', models.TextField()),
                ('expressive_language', models.TextField()),
                ('provisional_diagnosis', models.TextField()),
                ('recommendations', models.TextField()),
                ('reels_RL_score', models.IntegerField()),
                ('reels_EL_score', models.IntegerField()),
                ('tests_administered', models.CharField(default='REELS', max_length=100)),
                ('Status', models.CharField(default='Not Started', max_length=50)),
                ('email_sent', models.BooleanField(default=False)),
                ('clienttable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.clienttable')),
            ],
        ),
        migrations.CreateModel(
            name='OTAssesment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('therapist', models.CharField(max_length=100)),
                ('date_of_assessment', models.DateField()),
                ('presenting_complaints', models.TextField()),
                ('milestone_development', models.TextField()),
                ('behavior_cognition', models.TextField()),
                ('cognitive_skills', models.TextField()),
                ('kinaesthesia', models.TextField()),
                ('Status', models.CharField(default='Not Started', max_length=50)),
                ('email_sent', models.BooleanField(default=False)),
                ('clienttable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.clienttable')),
            ],
        ),
        migrations.CreateModel(
            name='Assesment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('therapist', models.CharField(max_length=100)),
                ('date_of_assessment', models.DateField()),
                ('prenatal_history', models.TextField()),
                ('family_history', models.TextField()),
                ('development_history', models.TextField()),
                ('school_history', models.TextField()),
                ('tests_administered', multiselectfield.db.fields.MultiSelectField(choices=[('DST', 'DST'), ('VSMS', 'VSMS'), ('MISIC', 'MISIC')], max_length=100)),
                ('test_results', models.IntegerField()),
                ('behavioural_observation', models.TextField()),
                ('impression', models.TextField()),
                ('recommendations', models.TextField()),
                ('created_on', models.DateField(auto_now=True)),
                ('created_by', models.CharField(max_length=200)),
                ('modified_on', models.DateTimeField(blank=True, null=True)),
                ('modified_by', models.CharField(max_length=200)),
                ('email_sent', models.BooleanField(default=False)),
                ('version', models.CharField(max_length=10)),
                ('Status', models.CharField(default='Not Started', max_length=50)),
                ('clienttable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.clienttable')),
            ],
        ),
    ]
