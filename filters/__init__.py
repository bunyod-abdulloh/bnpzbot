from loader import dp
from .admins import AdminFilter

if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
