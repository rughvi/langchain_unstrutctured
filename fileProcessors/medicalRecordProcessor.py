from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from models.medicalRecord import MedicalRecord

class MedicalRecordProcessor:
    def processText(self, filePath):
        print('processText called')
        loaders = [UnstructuredPDFLoader(filePath)]
        index = VectorstoreIndexCreator().from_loaders(loaders)
        
        name = index.query('name?')
        print('name is : ' + name)
        
        address = index.query('address?')
        print('address is : ' + address)

        homePhoneNumber = index.query('Home phone?')
        print('home phone number is : ' + homePhoneNumber)

        workPhoneNumber = index.query('Work phone?')
        print('work phone number is : ' + workPhoneNumber)

        return MedicalRecord(name, address, homePhoneNumber, workPhoneNumber)