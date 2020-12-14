from django.db import models


# Create your models here.
class Especialidad(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name='Especialidad'
        verbose_name_plural='Especialidades'


class Horario(models.Model):
    day = models.CharField(verbose_name="Dia", max_length=100)
    horaIngreso = models.CharField(verbose_name="Hora de ingreso", max_length= 100)
    horaSalida = models.CharField(verbose_name="Hora de salida" ,max_length= 100)

    def __str__(self):
        return "{0} {1} {2}".format(self.day, self.horaIngreso, self.horaSalida)

    class Meta:
        verbose_name='Horario'
        verbose_name_plural='Horarios'


class Medico(models.Model):
    horario_id = models.ForeignKey(Horario, on_delete=models.CASCADE, verbose_name="Horario")
    especialidad_id = models.ForeignKey(Especialidad, on_delete=models.CASCADE, verbose_name="especidalidad del medico")
    NameD = models.CharField(verbose_name= "nombre", max_length=100)
    LastNameD = models.CharField(verbose_name="Apellido", max_length=100)

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.horario_id, self.especialidad_id, self.NameD, self.LastNameD)

    class Meta:
        verbose_name='Medico'
        verbose_name_plural='Medicos'


class Paciente(models.Model):
    Name = models.CharField(verbose_name='nombre', max_length=100)
    lastName = models.CharField(verbose_name='apellidos', max_length=100)
    age = models.IntegerField(verbose_name= "edad")
    DNI = models.IntegerField(verbose_name='DNI', unique=True)
    seguro = models.IntegerField(verbose_name='seguro', unique=True)
    telefono = models.IntegerField(verbose_name = 'telefono', unique = True)

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5}".format(self.Name, self.lastName, self.age, self.DNI, self.seguro, self.telefono)

    class Meta:
        verbose_name='Paciente'
        verbose_name_plural='Pacientes'


class Cita(models.Model):
    medico_id = models.ForeignKey(Medico,  on_delete=models.CASCADE, verbose_name="Medico")
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name= "Paciente")
    Fecha = models.DateTimeField(blank=True)

    def __str__(self):
        return "{0} {1} {2}".format(self.medico_id, self.paciente_id, self.Fecha)

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural='Citas'
