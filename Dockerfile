#
#    Dockerfile is part of Demo MisionTIC-2021 C4, created by Carlos Andrés Sierra.
#
#    Demo MisionTIC-2021 C4 is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Demo MisionTIC-2021 C4 is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Demo MisionTIC-2021 C4. If not, see <https://www.gnu.org/licenses/>.
#
#    For contact, you can write to casierrav@unal.edu.co
#


#setup env
FROM python:3.8
ENV PYTHONUNBUFFERED 1
#copy data
RUN mkdir /users
WORKDIR /users
ADD . /users/ 
#install python packages
RUN pip install -r requirements.txt
#execute DRF application
EXPOSE 8080
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT