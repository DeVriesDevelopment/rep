import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# Fetch the service account key JSON file contents
cred = credentials.Certificate('lib/serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://marcobot-5ba87.firebaseio.com/'
})

def firebase_get(table, where = None):
    if(where == None):
        return db.reference(table).get()
    else:
        ref = db.reference(table)
        if(where[1] == 'key'):
            snapshot = ref.order_by_key().equal_to(where[2]).get()
            return snapshot
        else:
            if(where[0] == "eq"):
                snapshot = ref.order_by_child(where[1]).equal_to(where[2]).get()
                return snapshot
            if (where[0] == "gt"):
                snapshot = ref.order_by_child(where[1]).start_at(where[2]).get()
                return snapshot
            if (where[0] == "lt"):
                snapshot = ref.order_by_child(where[1]).end_at(where[2]).get()
                return snapshot
            if (where[0] == "order_by_key"):
                snapshot = ref.order_by_key().get()
                return snapshot
            if (where[0] == "order_by_child"):
                snapshot = ref.order_by_child(where[1]).get()
                return snapshot


def firebase_create(table, data, push = False):
    postRef = db.reference(table)
    if(push == True):
        postRef = postRef.push()
    postRef.set(data);

def firebase_delete(table, key):
    ref = db.reference(table)
    ref.child(key).delete()

def firebase_update(table, data):
    ref = db.reference(table)
    ref.update(data);
