import uuid

class User:

   # def __init__(self, first_name, last_name, id, age, lat, lng ):
    #    self.uuid = uuid.uuid4()
     #   self.first_name = first_name
      #  self.last_name = last_name
       # self.id = id
        #self.age = age
        #self.lat = lat
        #self.lng = lng



    def __init__(self, id, first_name, last_name):
        self.uuid = uuid.uuid4()
        self._id = id
        self._first_name = first_name
        self._last_name = last_name

    def __repr__(self):
        return f"User with ID: {self._id} -> {self._first_name} {self._last_name} \n"
