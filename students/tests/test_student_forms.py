from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse

from students.models import Student, Group

@override_settings(LANGUAGE_CODE='en')

class TestStudentUpdateForm(TestCase):
    fixtures = ['students_test_data.json']

    def setUp(self):
        #remember test browser
        self.client = Client()

        #remember utl to edit form
        self.url = reverse('students_edit', kwargs={'pk': 1})

    def test_form(self):
        #login as admin to access student edit form
        self.client.login(username='admin', password='admin')

        #get form and check few fields there
        response = self.client.get(self.url)

        #check response status
        self.assertEqual(response.status_code, 200)

        #check page title, fwe field titles and vutton on edit form
        self.assertIn('Edit Student', response.content)
        self.assertIn('Ticket', response.content)
        self.assertIn('Last Name', response.content)
        self.assertIn('name="add_button"', response.content)
        self.assertIn('name="cancel_button"', response.content)
        self.assertIn('action="%s"' % self.url, response.content)
        self.assertIn('podoba.jpg', response.content)

    def test_success(self):
        #login as admin to access student edit form
        self.client.login(username='admin', password='admin')

        #post form with valid data
        group = Group.objects.filter(title='Group1')[0]
        response = self.client.post(self.url, {
            'first_name': 'Updated Name',
            'last_name': 'Updated Last Name',
            'ticket': '567',
            'student_group': group.id,
            'birthday': '1990-11-11'}, follow=True)

        #check response status
        self.assertEqual(response.status_code, 200)

        #test updated student details
        student = Student.objects.get(pk=1)
        self.assertEqual(student.first_name, 'Updated Name')
        self.assertEqual(student.last_name, 'Updated Last Name')
        self.assertEqual(student.ticket, '567')
        self.assertEqual(student.student_group, group)

        #check proper redirect after form post
        self.assertIn('Student edited successfully', response.content)
        
    def test_access(self):
        #try to access form as anonymous user
        response = self.client.get(self.url, follow=True)

        #we have to get 200 code and login form
        self.assertEqual(response.status_code, 200)
