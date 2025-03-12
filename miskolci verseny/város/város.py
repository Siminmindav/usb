import csv
from datetime import datetime

import random

def unexpected_event(city):
    events = [
        {"name": "Nothing happened", "probability": 0.5, "budget_change": 0, "satisfaction_change": 0},
        {"name": "Economic boom", "probability": 0.2, "budget_change": 50000, "satisfaction_change": 10},
        {"name": "Natural disaster", "probability": 0.1, "budget_change": -100000, "satisfaction_change": -20},
        {"name": "New business opening", "probability": 0.1, "budget_change": 30000, "satisfaction_change": 5},
        {"name": "Protest in the city", "probability": 0.1, "budget_change": -20000, "satisfaction_change": -5}
    ]

    event = random.choices(events, [e['probability'] for e in events])[0]
    print(f"Unexpected event: {event['name']}")
    city.budget += event['budget_change']
    city.satisfaction += event['satisfaction_change']


def build_new_building(city):
    print("Enter building type (e.g., Residential, Commercial):")
    building_type = input()
    print("Enter the cost of the new building:")
    cost = float(input())

    # Check if enough budget is available
    if city.budget < cost:
        print("Not enough budget!")
        return

    print("Building started.")
    new_building = Building(len(city.buildings) + 1, building_type, 1, 100)
    city.buildings.append(new_building)
    city.budget -= cost

def maintain_building(city):
    print("Enter the building ID to maintain:")
    building_id = int(input())
    building = next((b for b in city.buildings if b.id == building_id), None)
    
    if building is None:
        print("Building not found.")
        return
    
    print("Maintaining building.")
    building.repair()
    city.budget -= 5000  # Example maintenance cost

def add_service(city):
    print("Enter the service name:")
    service_name = input()
    print("Enter the monthly cost of the service:")
    cost = float(input())

    # Add the service
    service = Service(len(city.services) + 1, service_name, cost)
    city.services.append(service)
    city.budget -= cost

def remove_service(city):
    print("Enter the service ID to remove:")
    service_id = int(input())
    service = next((s for s in city.services if s.id == service_id), None)
    
    if service is None:
        print("Service not found.")
        return
    
    city.services.remove(service)
    city.budget += service.cost  # Save on the monthly cost


class City:
    def __init__(self, budget, satisfaction, min_satisfaction, buildings, services, projects):
        self.budget = budget
        self.satisfaction = satisfaction
        self.min_satisfaction = min_satisfaction
        self.buildings = buildings  # list of Building objects
        self.services = services  # list of Service objects
        self.projects = projects  # list of Project objects
        self.month = 0  # Current month in the simulation

    def load_from_csv(self, buildings_file, services_file, projects_file):
        # Load buildings
        with open(buildings_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                building = Building(row['id'], row['name'], int(row['condition']), int(row['area']))
                self.buildings.append(building)

        # Load services
        with open(services_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                service = Service(row['id'], row['name'], float(row['cost']))
                self.services.append(service)

        # Load projects
        with open(projects_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                project = Project(int(row['id']), row['name'], float(row['cost']), row['start_date'], row['end_date'], row['affected_buildings'])
                self.projects.append(project)

    def save_state(self, filename):
        with open(filename, 'a') as file:
            file.write(f"Month {self.month}, Budget: {self.budget}, Satisfaction: {self.satisfaction}\n")
            for building in self.buildings:
                file.write(f"Building {building.name}: {building.condition}\n")
            for service in self.services:
                file.write(f"Service {service.name}: {service.cost}\n")

class Building:
    def __init__(self, id, name, condition, area):
        self.id = id
        self.name = name
        self.condition = condition
        self.area = area

    def repair(self):
        # Increase the condition of the building
        self.condition = min(self.condition + 1, 5)

class Service:
    def __init__(self, id, name, cost):
        self.id = id
        self.name = name
        self.cost = cost

class Project:
    def __init__(self, id, name, cost, start_date, end_date, affected_buildings):
        self.id = id
        self.name = name
        self.cost = cost
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.affected_buildings = list(map(int, affected_buildings.strip('{}').split(',')))

    def is_completed(self, current_month):
        # Check if project has been completed
        return current_month >= (self.end_date.month)

def main():
    city = City(budget=1000000, satisfaction=75, min_satisfaction=50, buildings=[], services=[], projects=[])
    city.load_from_csv('buildings.csv', 'services.csv', 'projects.csv')

    # Simulate the game for 12 months
    for month in range(1, 13):
        city.month = month
        print(f"Month {month}")
        city.save_state('simulation_log.txt')

if __name__ == "__main__":
    main()

