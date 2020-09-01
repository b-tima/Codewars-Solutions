public class Dinglemouse
{
  private string firstName;
  private string lastName;
  public string FullName
  {
    get
    {
      if(firstName == string.Empty) return lastName;
      else if(lastName == string.Empty) return firstName;
      else if(lastName == string.Empty && firstName == string.Empty) return string.Empty;
      return firstName+" "+lastName;
    }
  }
  
  public Dinglemouse(string firstName, string lastName)
  {
    this.firstName = firstName;
    this.lastName = lastName;
  }
}